# Project instructions: Nadine Holländer

## Reminder explicitly requested by the user
At the start of the NEXT substantive extension of this website (new pages, new services, forms, bookings, analytics, maps/videos, externally loaded fonts, or hosting/email changes), briefly remind Philipp to review and update Impressum and Datenschutz. Carry that review into the work and inspect whether the change adds data processing or legal information duties. This is an event-triggered project reminder, not a recurring scheduled task. Do not repeatedly remind during the current cleanup task.

## Confirmed state (6 November 2026)
- Sole operator and data controller: Nadine Holländer, address/contact as in the legal pages.
- Freelance; no USt-ID according to the user. Do not infer § 19 UStG status or absence of a Wirtschafts-ID from freelance/low-volume activity.
- No regulated profession. No obligation/willingness for consumer dispute resolution.
- Photo credit requested: Fotos: Nadine Holländer.
- Contact data/documents only for requests, their handling and contracted care/consulting; no advertising use.
- IONOS production deployment is explicitly authorized. AVV exists. First upload was postponed by user because the IONOS email confirmation code was unavailable; do not claim production deployment succeeded. Also check www DNS and HTTPS certificate before launch.
- No cookies/local storage/third-party client-side tracking, forms, maps, videos or remotely loaded fonts in the current implementation. Recheck after extensions, including any host-provided statistics.
- Nadine is the data controller/contact for privacy questions; do not label her her own independent Datenschutzbeauftragte.

## Hosting variants and deploy
The committed visitor text and `content/hosting-ionos.html` contain the finished IONOS version. `scripts/build-ionos.py --target pages` substitutes `content/hosting-github.html` when publishing to GitHub Pages, so both hosts have factual text with no migration/preview wording. `--target ionos` (default) generates the production package. GitHub stays noindex. Deployment is manually triggered through `.github/workflows/deploy-ionos.yml` or `scripts/deploy-ionos.py`. Credentials must be environment/repository secrets or in-memory stdin, never tracked files. A pinned SSH host-key fingerprint and explicit remote directory are required. Do not change passwords or create credentials on the user's behalf through the browser.

## Internal launch follow-up (not visitor-facing placeholders)
Verify any assigned Wirtschafts-ID / register entry, actual IONOS product/log retention/statistics configuration, and actual email provider/retention and transfers against the contracts. The site uses only the confirmed no-USt-ID statement, without making a claim that no Wirtschafts-ID exists. User-supplied credit is not a blanket license declaration. Assess any duty to appoint an independent DSB against actual business processing, rather than self-appointment.
