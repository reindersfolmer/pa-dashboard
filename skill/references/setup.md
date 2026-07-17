# Eerste-run setup

Doorloop dit één keer, samen met David (dit is per definitie een interactieve run — stel vragen waar nodig). Doel: werkende config in Dropbox, een publicerend webadres, en een uurplanning.

## 1. GitHub-account en repo (David doet dit zelf, jij loodst hem erdoorheen)

Geef David deze stappen, één voor één, en wacht per stap op bevestiging:

1. Maak een gratis account op https://github.com/signup (e-mailadres bevestigen).
2. Maak een nieuwe repository: https://github.com/new — naam `pa-dashboard`, zichtbaarheid **Public** (vereist voor gratis GitHub Pages; de inhoud is versleuteld dus dit is veilig), vink "Add a README file" aan, klik *Create repository*.
3. Zet GitHub Pages aan: in de repo → *Settings* → *Pages* → onder "Build and deployment" kies *Deploy from a branch*, branch `main`, map `/ (root)`, *Save*. Het webadres wordt `https://<gebruikersnaam>.github.io/pa-dashboard/`.
4. Maak een toegangstoken: https://github.com/settings/personal-access-tokens/new — naam `pa-dashboard`, vervaldatum 1 jaar, *Only select repositories* → `pa-dashboard`, bij *Repository permissions* alleen **Contents: Read and write**. Genereer en plak het token (begint met `github_pat_`) in de chat.

Leg uit waarom het token zo krap is: het kan alléén bestanden in deze ene repo schrijven, niets anders in zijn account.

## 2. Wachtwoord en VIP-lijst

- Vraag David een dashboardwachtwoord te kiezen (in de chat). Adviseer: niet een wachtwoord dat hij elders gebruikt — het staat in de config in zijn Dropbox.
- De VIP-lijst heeft een vaste basis: **iedereen binnen Davids eigen organisaties** (vip_domeinen — bevestig de domeinen: excitehotels.nl, het Urban Residences-domein, en eventueel THP/IFHG) plus **Menno Bos, Roderik, Taco en Marcel Groeskamp** (vraag hun mailadressen of herken ze op naam). Vraag of er nog iemand bij moet; hij kan later altijd zeggen "voeg X toe aan mijn VIP's".

## 3. Config en state wegschrijven

Maak in Dropbox de map `/PA Dashboard/` met:

```json
// config.json
{
  "github": { "owner": "<gebruikersnaam>", "repo": "pa-dashboard", "token": "github_pat_..." },
  "pages_url": "https://<gebruikersnaam>.github.io/pa-dashboard/",
  "wachtwoord": "<gekozen wachtwoord>",
  "vips": [ { "naam": "Menno Bos" }, { "naam": "Roderik" }, { "naam": "Taco" }, { "naam": "Marcel Groeskamp" } ],
  "vip_domeinen": ["excitehotels.nl", "<urban-domein>"],
  "werkdag": { "dagen": "ma-vr", "van": "07:00", "tot": "19:00", "tijdzone": "Europe/Amsterdam" }
}
```

en een lege `state.json`: `{ "cache": {}, "items": [], "run_log": [] }`.

## 4. Uurplanning aanmaken

Maak een scheduled task via `mcp__claude-code-remote__create_trigger` (nooit de lokale cron-tools — die overleven de sessie niet):

- naam: `PA Dashboard uurlijkse run`
- cron: elk uur binnen Davids werkdag, ma–vr. **Let op de tijdzone**: bepaal eerst met bash het actuele verschil tussen UTC en Europe/Amsterdam en reken 07:00–19:00 lokaal om naar UTC-uren (zomertijd: `0 5-17 * * 1-5`).
- prompt (zelfstandig leesbaar, elke firing is een verse sessie):
  > "Werk Davids PA-dashboard bij volgens de skill pa-dashboard. Dit is een geplande, onbeheerde run: stel geen vragen, gebruik cache voor onbereikbare bronnen, en publiceer het resultaat naar GitHub Pages."

Maak daarnaast een tweede scheduled task voor de weekreview:

- naam: `PA Dashboard weekreview`
- cron: vrijdag 16:00 lokale tijd (omgerekend naar UTC)
- prompt:
  > "Draai de wekelijkse review van Davids PA-dashboard volgens de skill pa-dashboard (references/leren.md, sectie weekreview): expertpanel over het leerlog en de gebruikshistorie, maximaal 5 voorstellen, publiceer als Weekvoorstellen op het dashboard. Onbeheerde run — stel geen vragen."

## 5. Eerste publicatie en test

1. Draai direct een volledige run (Chrome staat nu waarschijnlijk open — mooi moment om ook Urban/WhatsApp/Google-agenda te vullen).
2. Laat David het webadres openen en het wachtwoord testen.
3. Geef hem de mobiele instructie: open het adres in Safari op zijn iPhone → deelknop → **Zet op beginscherm**. Daarna opent het dashboard als app.
4. Tip voor later (optioneel, maakt Urban/Google-agenda ook in geplande runs bereikbaar): deel de Urban-agenda en Google-agenda eenmalig met david@excitehotels.nl; test daarna of `outlook_calendar_search` ze ziet.
