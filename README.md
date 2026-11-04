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
