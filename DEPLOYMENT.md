# Veröffentlichung bei IONOS

Die Website ist statisch. Derselbe Build kann von einem Rechner, diesem Chat oder einem GitHub-Repository mit den berechtigten Zugangsdaten hochgeladen werden. IONOS-Produktion und GitHub Pages zeigen auf ausdrücklichen Nutzerwunsch beide den für die Hauptdomain vorbereiteten IONOS-Datenschutzabschnitt. Die Seiten enthalten keine Umzugs- oder Entwurfshinweise.

## Status

Der erste Server-Upload steht noch aus: Die IONOS-Kontoanmeldung verlangt einen per E-Mail versandten Bestätigungscode. Der Nutzer hat diesen Schritt auf später verschoben. In der ursprünglichen E-Mail liegt nur der IONOS-Kontozugang, kein SFTP-Zugang. Am 6. November 2026 zeigte die Domain ohne www auf IONOS; für www lieferte die DNS-Abfrage keinen A-Eintrag, und HTTPS der Domain ohne www war noch nicht funktionsfähig. Vor der Freischaltung im Konto kontrollieren.

## Benötigte Angaben

Diese Werte als lokale Umgebungsvariablen oder GitHub Actions **Secrets** bereitstellen. Keine Zugangsdaten, private Schlüssel oder `.env`-Dateien committen.

| Name | Inhalt |
| --- | --- |
| `IONOS_SFTP_HOST` | Im IONOS-Konto angegebener SFTP-Server |
| `IONOS_SFTP_USER` | SFTP-Benutzer, nicht der Portal-Login |
| `IONOS_SFTP_PASSWORD` | Passwort des SFTP-Benutzers; alternativ Schlüssel |
| `IONOS_SFTP_KEY` | Optional: privater SSH-Schlüssel statt Passwort; lokal auch Dateipfad möglich |
| `IONOS_SFTP_PATH` | Explizites absolutes Verzeichnis, auf das die Domain zeigt |
| `IONOS_SFTP_FINGERPRINT` | Über einen vertrauenswürdigen Kanal bestätigter SHA256-Fingerabdruck des Servers |
| `IONOS_SFTP_PORT` | Optional; Standard 22 |
| `IONOS_SITE_URL` | Optional; Standard `https://www.nadinehollaender.de/` |

Fingerprint aus einer von IONOS bestätigten Quelle abgleichen. Das bloße ungeprüfte Ergebnis von `ssh-keyscan` reicht nicht als Bestätigung. Zugang auf das Website-Verzeichnis begrenzen, soweit das Hosting dies erlaubt.

## Lokal / aus diesem Chat

```sh
python3 -m venv .venv-deploy
.venv-deploy/bin/python -m pip install -r scripts/requirements-deploy.txt
.venv-deploy/bin/python scripts/deploy-ionos.py --build-only
.venv-deploy/bin/python scripts/deploy-ionos.py --dry-run
.venv-deploy/bin/python scripts/deploy-ionos.py
```

Der Dry-Run prüft die SFTP-Verbindung und Ziel-Dateien, verändert aber keine Serverdateien. Ohne gesetztes Passwort/Schlüssel fragt das Skript im interaktiven Terminal verdeckt nach dem Passwort. Für eine geschützte Übergabe zwischen Tools kann `--config-stdin` ein JSON-Objekt aus stdin entgegennehmen (Schlüssel: `sftp_host`, `sftp_user`, `sftp_password` oder `sftp_key`, `sftp_path`, `sftp_fingerprint`, optional `sftp_port`, `site_url`). Das JSON nicht in einer Datei speichern oder ausgeben.

Beim Upload werden ausschließlich die generierten HTML-, CSS-, JS-, Bild-, Favicon-, Robots- und Sitemap-Dateien übertragen. Vorhandene betroffene Dateien werden lokal unter `work/deploy-backups/` gesichert. Fremde Serverdateien werden nicht gespiegelt oder gelöscht. Einzeldateien werden nach Möglichkeit atomar ersetzt; der Deployment-Marker wird zuletzt geschrieben. Bei einem Teilfehler kann eine Wiederherstellung der gesicherten Dateien erforderlich sein. Nach Abschluss wird die Release-ID über HTTPS geprüft. Ein fehlgeschlagener HTTPS-Check bedeutet nicht automatisch, dass keine Dateien hochgeladen wurden.

## Direkt in diesem GitHub-Repository

Secrets unter Settings → Secrets and variables → Actions hinterlegen. Anschließend unter Actions den Workflow **Deploy to IONOS** starten. Der erste Lauf ist standardmäßig ein Dry-Run. Zum Upload `dry_run` ausschalten. Es gibt absichtlich keinen automatischen Server-Upload bei jedem Push.

## Aus einem eigenen GitHub-Repository

Das andere Repository kann die Secrets bei sich speichern und den wiederverwendbaren Workflow aufrufen. Beispiel einer dortigen Datei `.github/workflows/deploy-website.yml`:

```yaml
name: Website veröffentlichen
on:
  workflow_dispatch:
    inputs:
      dry_run:
        type: boolean
        default: true
permissions:
  contents: read
jobs:
  website:
    uses: klasphilipp-private/hollaender/.github/workflows/deploy-ionos.yml@main
    with:
      dry_run: ${{ inputs.dry_run }}
    secrets:
      IONOS_SFTP_HOST: ${{ secrets.IONOS_SFTP_HOST }}
      IONOS_SFTP_USER: ${{ secrets.IONOS_SFTP_USER }}
      IONOS_SFTP_PASSWORD: ${{ secrets.IONOS_SFTP_PASSWORD }}
      IONOS_SFTP_KEY: ${{ secrets.IONOS_SFTP_KEY }}
      IONOS_SFTP_PATH: ${{ secrets.IONOS_SFTP_PATH }}
      IONOS_SFTP_FINGERPRINT: ${{ secrets.IONOS_SFTP_FINGERPRINT }}
      IONOS_SFTP_PORT: ${{ secrets.IONOS_SFTP_PORT }}
      IONOS_SITE_URL: ${{ secrets.IONOS_SITE_URL }}
```

Der Workflow lädt den aktuellen Website-Stand aus `klasphilipp-private/hollaender`, nicht die Dateien des aufrufenden Repositorys. Zum Einfrieren der Workflow-Definition kann statt `@main` ein geprüfter Commit verwendet werden; die Website-Dateien werden weiterhin aus `main` geladen. Die beiden Upload-Läufe desselben Repositorys werden serialisiert. Bei Aufrufen aus verschiedenen Repositorys müssen die Beteiligten sich abstimmen, damit kein paralleler Upload erfolgt.

## Rechtstexte bei späteren Änderungen

Bei neuen Seiten, Formularen, Online-Buchungen, Analysewerkzeugen, eingebetteten Inhalten, E-Mail- oder Hostingwechseln Impressum und Datenschutz erneut prüfen. Die Erinnerung ist in AGENTS.md hinterlegt. Die vorliegende AVV mit IONOS ist vom Nutzer bestätigt; konkrete Produkt- und Protokolleinstellungen vor dem ersten Upload prüfen.
