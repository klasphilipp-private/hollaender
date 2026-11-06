# Nadine Holländer – Website

Gewählte Gestaltung: ehemaliger Entwurf 3. Die Website liegt jetzt direkt in `index.html`; die übrigen Entwürfe und die Auswahlübersicht wurden entfernt.

- Überschrift: **Veränderung beginnt mit einer neuen Perspektive.**
- Haltung: **Strukturiert. Zugewandt. Authentisch.**
- Vorschau: https://klasphilipp-private.github.io/hollaender/
- Spätere Hauptdomain: https://www.nadinehollaender.de/

## SEO

Title: **Nadine Holländer | Beratung & Mediation in Recklinghausen**

Beschreibung: **Veränderung beginnt mit einer neuen Perspektive. Nadine Holländer – systemische Beraterin und zertifizierte Mediatorin in Recklinghausen. Jetzt Kontakt aufnehmen.**

Enthalten sind Canonical, Open-Graph-/Twitter-Angaben, Fotobeschreibung und Bildabmessungen sowie strukturierte Daten für Person, Website, Webseite und Porträt. Die SEO-Werte stehen zusätzlich in `seo.json`.

Die Pages-Vorschau bleibt mit `noindex,follow` von der Indexierung ausgeschlossen. `robots.txt` erlaubt den Abruf, damit Suchmaschinen das Noindex lesen können. Bild-Metadaten verweisen in der Vorschau auf das bereits erreichbare Pages-Foto. Canonical und Identität beziehen sich auf die spätere Hauptdomain.

## IONOS-Paket

`python3 scripts/build-ionos.py` erzeugt außerhalb des Repositorys unter `../outputs/ionos` die statische Übergabe. Das Paket verwendet ausschließlich die spätere Hauptdomain für absolute URLs, schaltet Indexierung frei und enthält Robots-Datei und Sitemap einschließlich Foto.

Vor dem tatsächlichen IONOS-Start vollständiges Impressum und Datenschutzhinweise ergänzen, Vorschauhinweise entfernen sowie finale Texte, Bildnutzungsrechte und Webfont klären. Nach Veröffentlichung Sitemap in der Google Search Console einreichen. Das Paket ist für die spätere Veröffentlichung vorbereitet; IONOS wurde nicht verändert.

Google entscheidet selbst über den angezeigten Titel, Beschreibungstext und ein mögliches Vorschaubild. Die Suchergebnisgrafik ist eine Illustration, kein Nachweis einer Indexierung.

## Gestaltung

Farbfächer: Petrol `#006D82`, Blau `#8AB7C2`, Hellblau `#E2EDEF`, Schwarz und Weiß. Original-Logo, SVG-Pfeile, Logo-Signet als Favicon. Akzidenz Grotesk wird bis zur Lieferung einer lizenzierten Webfont durch Helvetica/Arial ersetzt. Keine Analysewerkzeuge, Cookies oder extern geladenen Schriften.

Mails, Zugangsdaten und unbearbeitete Quelldokumente gehören nicht in dieses Repository.

## Vorbereitete Rechtstexte und Header

`impressum.html` und `datenschutz.html` sind vom Footer jeder Seite erreichbar. Hellblaue Kästen mit der Beschriftung „Vor dem Start klären“ kennzeichnen unbestätigte Angaben. Die Seiten bleiben auch im IONOS-Paket vorerst auf `noindex`, bis die Texte vervollständigt und geprüft sind.

Offen: Wirtschafts-ID und etwaiger Registereintrag; Bildnachweis und Bildrechte; ggf. Datenschutzbeauftragte Person; Hostingvertrag und Log-Fristen; E-Mail-Dienst und Löschfristen; finale technische Dienste. Nicht zutreffende optionale Abschnitte vor dem Start entfernen. Der aktuelle GitHub-Host und der geplante IONOS-Host sind getrennt beschrieben.

Der gemeinsame Header ist sticky mit transparentem Weiß und Hintergrundunschärfe. Ab 120 px Scrollposition verkleinert er sich; beim Rückweg unter 40 px wird er wieder größer. Die Hysterese verhindert Flackern. Bewegungsreduktion wird berücksichtigt. Der Navigationsbereich kann später weitere Links aufnehmen.

Recherchegrundlagen (4. November 2026):
- § 5 DDG: https://www.gesetze-im-internet.de/ddg/__5.html
- § 36 VSBG: https://www.gesetze-im-internet.de/vsbg/__36.html
- DSGVO: https://eur-lex.europa.eu/eli/reg/2016/679/oj?locale=de
- LDI NRW: https://www.ldi.nrw.de/
- GitHub: https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement
- IONOS Anbieter: https://www.ionos.de/impressum.html
- IONOS Logdateien: https://www.ionos.de/hilfe/hosting/log-dateien/hinweise-zu-logdateien/
- IONOS Auftragsverarbeitung: https://www.ionos.de/hilfe/index.php?id=3212

## Übernommene Rückmeldung vom 6. November 2026

- Anbieterin als Einzelperson und Geschäftsadresse bestätigt.
- Keine USt-ID laut Rückmeldung. Das begründet keine Aussage zu einer etwaigen Wirtschafts-ID oder einem Registereintrag; diese Restfragen bleiben markiert. Es wird keine unbelegte umsatzsteuerliche Einordnung veröffentlicht.
- Keine reglementierte Tätigkeit: zugehöriger offener Abschnitt entfernt.
- Keine Pflicht/Bereitschaft zur Verbraucherschlichtung: Erklärung eingetragen.
- Inhaltlich verantwortlich ist Nadine Holländer mit derselben Anschrift. Eine Benennung nach § 18 Abs. 2 MStV wird für diese reine Vorstellungsseite nicht behauptet; bei späteren journalistisch-redaktionellen Inhalten erneut prüfen.
- Bildnachweis und Rechte bleiben offen. Im Datenschutz nur die bestätigte Verantwortlichkeit/Adresse übernommen; keine Hosting- oder Löschfristen erfunden.
- Der Kontaktaufruf im Profil besteht aus zwei gleich großen Buttons untereinander: E-Mail und Telefonnummer (`tel:+491772425124`).
