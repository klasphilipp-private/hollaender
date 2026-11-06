# Nadine Holländer

Statische Website für https://www.nadinehollaender.de/. GitHub-Version: https://klasphilipp-private.github.io/hollaender/.

## Betrieb und Veröffentlichung

Serverpaket: `python3 scripts/build-ionos.py --output /absoluter/ausgabeordner`. GitHub-Paket: derselbe Aufruf mit `--target pages`. Die vorbereiteten IONOS-Rechtstexte werden auf ausdrücklichen Nutzerwunsch auch in der GitHub-Version angezeigt. Auf der Website stehen keine Umzugs-/Entwurfshinweise. Die GitHub-Version bleibt noindex; die IONOS-Hauptseite wird für Suchmaschinen freigegeben.

Lokaler und wiederverwendbarer SFTP-Upload: siehe [DEPLOYMENT.md](DEPLOYMENT.md). Zugangsdaten ausschließlich als Umgebungsvariablen, verdeckte Eingabe oder GitHub Actions Secrets. Der Nutzer hat den ersten IONOS-Upload wegen des noch fehlenden Bestätigungscodes auf später verschoben; ein erfolgreicher Server-Upload wird nicht behauptet.

## Rechtstexte und bestätigte Angaben

Besuchertexte in Impressum und Datenschutz sind von den Entwurfs-/Rückfragekästen befreit. Bestätigt sind Einzelbetreiberin und Geschäftsanschrift, fehlende USt-ID, keine reglementierte Tätigkeit, keine Verpflichtung/Bereitschaft zur Verbraucherschlichtung, Fotoangabe „Fotos: Nadine Holländer“, die vorliegende IONOS-AVV sowie die ausschließliche Nutzung von Anfragen/Dokumentationen für deren Bearbeitung und vereinbarte Betreuung.

Nadine wird als datenschutzrechtlich Verantwortliche und Ansprechpartnerin geführt; nicht als ihre eigene unabhängige Datenschutzbeauftragte. Aus der geringen freiberuflichen Tätigkeit wird kein §-19-UStG-Status und keine Aussage über eine Wirtschafts-ID abgeleitet. Die USt-ID-Angabe lautet nur, dass keine Nummer erteilt wurde. Interne Nachprüfpunkte stehen in AGENTS.md und nicht als Platzhalter in den Besuchertexten.

Bei zukünftigen Erweiterungen den Nutzer an die Aktualisierung von Impressum und Datenschutz erinnern und die konkreten Auswirkungen der neuen Inhalte/Dienste prüfen (expliziter Nutzerwunsch, siehe AGENTS.md).

## Gestaltung und SEO

Originalfarben: #006D82, #8AB7C2, #E2EDEF, Schwarz und Weiß. Lokale Logo-/Foto-Dateien, SVG-Pfeile, Signet-Favicon, zwei gleich große Kontaktbuttons im Profil. Transparenter sticky Header mit kompakter Scrollansicht. Helvetica/Arial als Ersatz für Akzidenz Grotesk bis zur Lieferung einer lizenzierten Webfont. Keine eigenen Cookies, Webspeicher oder eingebundenen Tracking-/Karten-/Video-Dienste.

Metadaten, Canonical und strukturierte Daten zu Person, Website und Foto sind in index.html hinterlegt; SEO-Werte zusätzlich in seo.json. Google entscheidet selbst über Titel, Snippet und Bildanzeige.

## Recherchegrundlagen

- § 5 DDG: https://www.gesetze-im-internet.de/ddg/__5.html
- § 36 VSBG: https://www.gesetze-im-internet.de/vsbg/__36.html
- DSB-Interessenkonflikte, Abschnitt 3.5: https://www.datenschutzkonferenz-online.de/media/wp/20170405_wp243_rev01.pdf
- IONOS Webhosting: https://www.ionos.de/hilfe/datenschutz/datenverarbeitung-durch-ihr-ionos-produktes/datenverarbeitung-durch-webhosting-produkte/
- IONOS AVV: https://www.ionos.de/hilfe/index.php?id=3212
- GitHub Datenschutz: https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement

Mails, Zugangsdaten und unbearbeitete Quelldokumente gehören nicht in dieses Repository.
