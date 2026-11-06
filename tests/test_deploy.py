import importlib.util
from pathlib import Path
import stat, tempfile, unittest
from types import SimpleNamespace

spec = importlib.util.spec_from_file_location('deploy', Path(__file__).resolve().parents[1]/'scripts/deploy-ionos.py')
deploy = importlib.util.module_from_spec(spec); spec.loader.exec_module(deploy)

class SFTP:
    def __init__(self, atomic=True, fail_new=False):
        self.files = {'/site/index.html': b'old', '/site/unrelated.txt': b'keep'}
        self.dirs = {'/', '/site'}
        self.atomic, self.fail_new = atomic, fail_new
        self.uploads = []
    def lstat(self, path):
        if path in self.dirs: return SimpleNamespace(st_mode=stat.S_IFDIR, st_size=0)
        if path not in self.files: raise FileNotFoundError(path)
        return SimpleNamespace(st_mode=stat.S_IFREG, st_size=len(self.files[path]))
    stat = lstat
    def mkdir(self, path): self.dirs.add(path)
    def get(self, path, local): Path(local).write_bytes(self.files[path])
    def put(self, local, path, confirm=True):
        self.files[path] = Path(local).read_bytes(); self.uploads.append(path)
    def posix_rename(self, source, target):
        if not self.atomic: raise OSError('unsupported')
        self.files[target] = self.files.pop(source)
    def rename(self, source, target):
        if self.fail_new and '.upload-' in source and target == '/site/index.html': raise OSError('injected failure')
        if target in self.files: raise OSError('exists')
        self.files[target] = self.files.pop(source)
    def remove(self, path): del self.files[path]

class DeployTests(unittest.TestCase):
    def run_upload(self, sftp, dry=False):
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp); local = folder/'new.html'; local.write_bytes(b'new')
            backup = folder/'backup'
            deploy.upload(sftp, [('index.html',local)], '/site', backup, dry)
            if not dry: self.assertEqual((backup/'index.html').read_bytes(),b'old')
    def test_pinned_key_mismatch_rejected(self):
        key=SimpleNamespace(asbytes=lambda:b'server-key')
        with self.assertRaises(ValueError): deploy.check_fingerprint('SHA256:wrong',key)
        deploy.check_fingerprint(deploy.fingerprint(key),key)
    def test_only_managed_file_replaced_with_backup(self):
        sftp=SFTP();self.run_upload(sftp)
        self.assertEqual(sftp.files['/site/index.html'],b'new')
        self.assertEqual(sftp.files['/site/unrelated.txt'],b'keep')
    def test_dry_run_has_no_writes(self):
        sftp=SFTP();before=dict(sftp.files);self.run_upload(sftp,True)
        self.assertEqual(sftp.files,before);self.assertEqual(sftp.uploads,[])
    def test_failed_fallback_restores_original(self):
        sftp=SFTP(atomic=False,fail_new=True)
        with self.assertRaises(OSError): self.run_upload(sftp)
        self.assertEqual(sftp.files['/site/index.html'],b'old')
        self.assertEqual(sftp.files['/site/unrelated.txt'],b'keep')
    def test_rejects_unexpected_file_and_traversal(self):
        with tempfile.TemporaryDirectory() as tmp:
            (Path(tmp)/'.env').write_text('not public')
            with self.assertRaises(ValueError): deploy.public_files(Path(tmp))
        with self.assertRaises(ValueError): deploy.remote_join('/site','../outside')

if __name__=='__main__': unittest.main()
