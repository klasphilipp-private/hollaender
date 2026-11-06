"""Build and upload this static website over pinned-host-key SFTP.

Credentials come only from environment variables, hidden prompts, or JSON stdin.
No directory mirroring/deletion; only the generated public files are uploaded.
"""
from pathlib import Path, PurePosixPath
import argparse, base64, hashlib, hmac, io, json, os, posixpath, shutil, stat
import subprocess, sys, tempfile, uuid
from urllib.request import urlopen

ROOT = Path(__file__).resolve().parents[1]
ASSET_SUFFIXES = {'.css', '.js', '.svg', '.jpg', '.jpeg', '.png', '.ico', '.webp', '.woff', '.woff2'}
PUBLIC_FILES = {'index.html', 'impressum.html', 'datenschutz.html', 'robots.txt', 'sitemap.xml', 'favicon.ico'}

def public_files(folder):
    result = []
    for p in sorted(folder.rglob('*')):
        if p.is_symlink():
            raise ValueError('Symbolic links are not deployable.')
        if not p.is_file():
            continue
        rel = p.relative_to(folder)
        if rel.as_posix() not in PUBLIC_FILES and not (
            rel.parts[0] == 'assets' and p.suffix.lower() in ASSET_SUFFIXES
            and not any(part.startswith('.') for part in rel.parts)
        ):
            raise ValueError('Unexpected file in public build: ' + rel.as_posix())
        result.append((rel.as_posix(), p))
    if not PUBLIC_FILES <= {name for name, _ in result}:
        raise ValueError('The public build is incomplete.')
    return result

def build(folder):
    subprocess.run([sys.executable, str(ROOT/'scripts/build-ionos.py'), '--output', str(folder)], check=True, stdout=subprocess.DEVNULL)
    files = public_files(folder)
    digest = hashlib.sha256()
    for name, p in files:
        digest.update(name.encode()); digest.update(hashlib.sha256(p.read_bytes()).digest())
    release = digest.hexdigest()
    (folder/'deployment.json').write_text(json.dumps({'release': release}, indent=2) + '\n')
    return files + [('deployment.json', folder/'deployment.json')], release

def fingerprint(key):
    return 'SHA256:' + base64.b64encode(hashlib.sha256(key.asbytes()).digest()).decode().rstrip('=')

def check_fingerprint(expected, key):
    if not expected.startswith('SHA256:') or not hmac.compare_digest(expected.rstrip('='), fingerprint(key)):
        raise ValueError('SFTP server fingerprint does not match the trusted configuration.')

def remote_join(root, rel):
    name = PurePosixPath(rel)
    if name.is_absolute() or '..' in name.parts:
        raise ValueError('Invalid relative public path.')
    return posixpath.join(root, rel)

def mkdirs(sftp, folder):
    try:
        attrs = sftp.lstat(folder)
        if not stat.S_ISDIR(attrs.st_mode):
            raise ValueError('Remote parent is not a directory.')
    except FileNotFoundError:
        parent = posixpath.dirname(folder)
        if parent != folder:
            mkdirs(sftp, parent)
        sftp.mkdir(folder)

def upload(sftp, files, remote_root, backup_dir, dry_run=False):
    """Back up all managed targets first. Never remove unrelated server files."""
    existing = set()
    for rel, _ in files:
        target = remote_join(remote_root, rel)
        try:
            attrs = sftp.lstat(target)
        except FileNotFoundError:
            continue
        if not stat.S_ISREG(attrs.st_mode):
            raise ValueError('A managed target is not a regular file: ' + rel)
        if attrs.st_size > 20 * 1024 * 1024:
            raise ValueError('Existing managed file exceeds backup size limit: ' + rel)
        existing.add(rel)
        if not dry_run:
            local = backup_dir / rel
            local.parent.mkdir(parents=True, exist_ok=True)
            sftp.get(target, str(local))
    if dry_run:
        return
    # Assets first, public HTML last. Each replacement is atomic when supported.
    ordered = sorted(files, key=lambda item: (item[0] == 'deployment.json', item[0].endswith('.html'), item[0]))
    for rel, local in ordered:
        target = remote_join(remote_root, rel)
        mkdirs(sftp, posixpath.dirname(target))
        temp = target + '.upload-' + uuid.uuid4().hex
        sftp.put(str(local), temp, confirm=True)
        if sftp.stat(temp).st_size != local.stat().st_size:
            raise ValueError('Uploaded size mismatch: ' + rel)
        try:
            sftp.posix_rename(temp, target)
        except OSError:
            # Standard SFTP rename cannot replace an existing target. Preserve it
            # on the server until the new file is in place, in addition to backup.
            prior = target + '.previous-' + uuid.uuid4().hex
            had_prior = rel in existing
            if had_prior:
                sftp.rename(target, prior)
            try:
                sftp.rename(temp, target)
            except Exception:
                if had_prior:
                    sftp.rename(prior, target)
                raise
            if had_prior:
                sftp.remove(prior)
        print('Uploaded ' + rel)

def read_config(use_stdin):
    if use_stdin:
        cfg = json.load(sys.stdin)
    else:
        cfg = {name: os.environ.get('IONOS_' + name.upper(), '') for name in
               ['sftp_host', 'sftp_port', 'sftp_user', 'sftp_password', 'sftp_key', 'sftp_path', 'sftp_fingerprint', 'site_url']}
    if not cfg.get('sftp_password') and not cfg.get('sftp_key') and sys.stdin.isatty() and not use_stdin:
        import getpass
        cfg['sftp_password'] = getpass.getpass('SFTP password (not saved): ')
    for key in ['sftp_host', 'sftp_user', 'sftp_path', 'sftp_fingerprint']:
        if not isinstance(cfg.get(key), str) or not cfg[key].strip():
            raise ValueError('Missing configuration: IONOS_' + key.upper())
    if not cfg.get('sftp_password') and not cfg.get('sftp_key'):
        raise ValueError('Set an SFTP password or private key via environment/stdin.')
    if not cfg['sftp_path'].startswith('/') or '..' in PurePosixPath(cfg['sftp_path']).parts:
        raise ValueError('IONOS_SFTP_PATH must be an absolute, explicitly selected web directory.')
    return cfg

def connect(cfg):
    import paramiko
    class Pin(paramiko.MissingHostKeyPolicy):
        def missing_host_key(self, client, hostname, key):
            check_fingerprint(cfg['sftp_fingerprint'], key)
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(Pin())
    private = cfg.get('sftp_key')
    pkey = None
    if private:
        key_text = private if '-----BEGIN' in private else Path(private).read_text()
        for cls in [paramiko.Ed25519Key, paramiko.ECDSAKey, paramiko.RSAKey]:
            try:
                pkey = cls.from_private_key(io.StringIO(key_text)); break
            except (paramiko.SSHException, ValueError):
                continue
        if pkey is None:
            raise ValueError('Private key could not be read.')
    client.connect(cfg['sftp_host'], port=int(cfg.get('sftp_port') or 22), username=cfg['sftp_user'],
                   password=cfg.get('sftp_password') or None, pkey=pkey, timeout=20,
                   auth_timeout=20, banner_timeout=20, look_for_keys=False, allow_agent=False)
    return client

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config-stdin', action='store_true')
    parser.add_argument('--dry-run', action='store_true', help='Verify connection and targets without changes')
    parser.add_argument('--build-only', action='store_true')
    parser.add_argument('--backup-dir', type=Path, default=ROOT/'work'/'deploy-backups'/uuid.uuid4().hex)
    args = parser.parse_args()
    cfg = None if args.build_only else read_config(args.config_stdin)
    with tempfile.TemporaryDirectory(prefix='hollaender-public-') as tmp:
        files, release = build(Path(tmp))
        print('Validated public build: ' + str(len(files)) + ' files; release ' + release[:12])
        if args.build_only:
            return
        client = connect(cfg)
        try:
            sftp = client.open_sftp()
            root = sftp.normalize(cfg['sftp_path'])
            upload(sftp, files, root, args.backup_dir.resolve(), args.dry_run)
            sftp.close()
        finally:
            client.close()
        if args.dry_run:
            print('Connection and targets verified. No server files changed.')
            return
        print('Upload finished. Previous managed files are backed up locally.')
        url = (cfg.get('site_url') or 'https://www.nadinehollaender.de/').rstrip('/') + '/deployment.json?release=' + release
        with urlopen(url, timeout=25) as response:
            public = json.load(response)
        if public.get('release') != release:
            raise ValueError('HTTPS release verification failed; uploaded files may already be present.')
        print('Verified deployment via HTTPS.')

if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        # Never echo connection exception details which could contain secrets.
        if isinstance(exc, ValueError):
            print(str(exc), file=sys.stderr)
        else:
            print('Deployment stopped (' + type(exc).__name__ + '). Check connection, credentials and HTTPS status; no credentials were printed.', file=sys.stderr)
        sys.exit(1)
