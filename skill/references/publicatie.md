# Versleutelen en publiceren

Het dashboard staat op GitHub Pages: een publieke repo, maar de inhoud is versleuteld met Davids wachtwoord. Alleen de versleutelde `index.html` gaat ooit de repo in — nooit de kale dashboard-HTML, nooit config.json of state.json, nooit het wachtwoord.

Benodigdheden uit `/PA Dashboard/config.json` (Dropbox):

```json
{
  "github": { "owner": "...", "repo": "pa-dashboard", "token": "github_pat_..." },
  "pages_url": "https://<owner>.github.io/pa-dashboard/",
  "wachtwoord": "..."
}
```

## Stap 1 — versleutelen

Schrijf de volledige dashboardpagina als `dashboard.html` (op basis van `assets/template.html`) en draai:

```bash
python3 <skill-pad>/scripts/build_page.py dashboard.html "<wachtwoord>" index.html
```

Het script vereist het Python-pakket `cryptography`; ontbreekt het, installeer dan eerst met `pip install cryptography --break-system-packages`. Het resultaat is één zelfstandige `index.html` met wachtwoordscherm; de inhoud is AES-256-GCM-versleuteld en wordt pas in de browser ontsleuteld.

Sanity-check vóór publicatie: `grep -c "PA-ENC" index.html` moet 1 opleveren en de kale dashboard-tekst (bijv. een afzendernaam) mag NIET in index.html voorkomen (`grep -c "<afzendernaam>" index.html` → 0).

## Stap 2 — pushen via git

Gebruik de git-route, niet de GitHub REST API — de Cowork-cloudomgeving laat `api.github.com` niet zomaar door, maar `git clone/push` over HTTPS met het token werkt wél:

```bash
TOKEN=...; OWNER=...; REPO=...   # uit config.json
cd /tmp && rm -rf pa-publish
git clone -q --depth 1 "https://x-access-token:$TOKEN@github.com/$OWNER/$REPO.git" pa-publish
cp index.html pa-publish/index.html
cd pa-publish
git -c user.name="PA Dashboard" -c user.email="pa-dashboard@noreply.local" \
    add index.html
git -c user.name="PA Dashboard" -c user.email="pa-dashboard@noreply.local" \
    commit -q -m "dashboard update" && git push -q
cd /tmp && rm -rf pa-publish
```

Een lege commit-melding ("nothing to commit") betekent dat de inhoud identiek is aan de vorige run — geen fout, gewoon klaar. GitHub Pages bouwt na een push binnen ± een minuut de nieuwe versie op het vaste adres uit `pages_url`. Probeer de live-URL níet met curl te controleren: de cloudomgeving laat verkeer naar `*.github.io` niet door. Een geslaagde push ís de verificatie (controleer desnoods met `git ls-remote` dat de nieuwe commit op main staat).

Faalt de git-route (bijv. netwerk of verlopen token): dashboard alsnog als bestand naar David sturen (SendUserFile) en de publicatiefout kort melden.

## Wachtwoordscherm-gedrag

De gegenereerde pagina onthoudt het wachtwoord optioneel op het apparaat ("onthoud op dit apparaat", localStorage) zodat David op zijn eigen telefoon niet elke keer hoeft in te loggen. Verkeerd wachtwoord → nette foutmelding, geen kapotte pagina.
