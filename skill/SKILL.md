---
name: pa-dashboard
description: David's persoonlijke PA-dashboard — leest Excite 365 (mail + agenda), Gmail, Urban 365 en WhatsApp (via Chrome) en Google-agenda uit, bepaalt prioriteiten, bereidt taken en vergaderingen voor, stelt concept-antwoorden op en publiceert alles als wachtwoordbeveiligde webapp op een vast webadres (desktop + mobiel). Gebruik deze skill ALTIJD wanneer David vraagt om zijn PA-dashboard, dashboard verversen, prioriteiten, dagoverzicht, "wat moet ik vandaag doen", briefing, takenlijst, of wanneer een geplande run vraagt het PA-dashboard bij te werken — ook als hij maar één onderdeel noemt (bijv. "zet die mail op mijn dashboard" of "snooze dat punt tot maandag").
---

# PA Dashboard

Dit is Davids digitale personal assistant. Elke run bouwt één actueel dashboard uit al zijn communicatiekanalen en publiceert dat naar een vast, wachtwoordbeveiligd webadres dat hij op desktop en telefoon opent. Het dashboard vertelt hem niet wát er allemaal is, maar wat er **nu toe doet** en wat hij eraan kan doen.

David runt meerdere hotelbedrijven (Excite Hotels, Urban Residences, THP/IFHG). Zijn dag is vol en versnipperd; de waarde van dit dashboard zit in scherpe selectie en voorbereid werk, niet in volledigheid. Tien prioriteiten is geen prioritering.

## Overzicht van een run

1. Lees config en state uit Dropbox (`/PA Dashboard/config.json` en `state.json`)
2. Lees alle bereikbare bronnen uit (parallel waar mogelijk) — zie `references/bronnen.md`
3. Prioriteer, bereid voor, stel concepten op (hieronder)
4. Bouw de dashboard-HTML op basis van `assets/template.html`
5. Versleutel en publiceer met `scripts/build_page.py` + git push — zie `references/publicatie.md`
6. Werk `state.json` bij (cache, uitstel-tracking, afgehandelde items)

**Eerste keer?** Als `/PA Dashboard/config.json` niet bestaat in Dropbox, is dit de eerste run: volg `references/setup.md` volledig (GitHub-account, repo, wachtwoord, VIP-lijst, doorlopende planning) voordat je iets anders doet.

## Config en state (Dropbox)

Dropbox is het geheugen van dit dashboard, omdat het ook bereikbaar is in geplande runs zonder desktop of Chrome.

- `/PA Dashboard/config.json` — VIP-lijst (personen én organisatiedomeinen: iedereen binnen Davids eigen organisaties is VIP), GitHub repo + token, dashboardwachtwoord, voorkeuren. Alleen wijzigen als David daarom vraagt ("voeg X toe aan mijn VIP's").
- `/PA Dashboard/state.json` — alles wat tussen runs onthouden moet worden:
  - `cache`: laatste snapshot per Chrome-bron (urban_mail, urban_agenda, whatsapp, google_agenda) mét ISO-timestamp
  - `items`: per gevolgd item een id, bron, eerste-gezien-datum, status (`open` / `afgevinkt` / `afgerond` / `gesnoozed tot <datum>` / `bewust geparkeerd`)
  - `run_log`: laatste paar runs met tijdstip en bronstatus
- `/PA Dashboard/leerlog.md` — wat het dashboard over Davids werkwijze heeft geleerd (zie `references/leren.md`). Groeit per afgerond item; wordt gelezen bij prioriteren en concepten schrijven.

Schrijf state.json aan het eind van élke run terug (Dropbox: delete + create_file, of overschrijven als de connector dat ondersteunt). Zonder die schrijfstap werkt uitstel-tracking en snoozen niet.

## Bronnen en degradatie

Details per bron staan in `references/bronnen.md`. Het principe:

- **Altijd bereikbaar** (ook in geplande runs): Excite 365 mail + agenda, Gmail, Dropbox.
- **Alleen bereikbaar als Davids Chrome met de Claude-extensie openstaat**: Urban-mailbox en -agenda (outlook.office.com), WhatsApp (web.whatsapp.com), Google-agenda (calendar.google.com).

Probeer bij elke run éérst of Chrome bereikbaar is (één snelle `tabs_context_mcp`-aanroep). Lukt dat niet, val dan zonder gedoe terug op de cache in state.json en toon op het dashboard per bron een statuschip: **vers** (deze run gelezen), **cache van HH:MM** of **niet beschikbaar**. Een dashboard met eerlijke bronstatus is bruikbaar; een run die faalt omdat één bron wegvalt niet. Blijf nooit hangen op een haperende bron: twee mislukte pogingen → cache gebruiken en door.

## Prioriteren

Bekijk alle open items (nieuwe mail van de laatste 3 werkdagen, alles wat in state.json nog `open` staat, agenda-items van vandaag en morgen, WhatsApp-berichten met een vraag of actie erin) en kies de items die David vandaag écht moeten bereiken. Maximaal 7, liever 5.

Weeg per item:

1. **Geld- en omzet-impact** — facturen, contracten, offertes, claims, huurkwesties. Hoe groter het bedrag of risico, hoe zwaarder. Noem het bedrag als het bekend is.
2. **Afzender** — mensen op de VIP-lijst in config.json wegen zwaar. Daarbuiten: verhuurders, investeerders, banken en advocaten zwaarder dan leveranciers en nieuwsbrieven.
3. **Uitstel** — gebruik de eerste-gezien-datum uit state.json. Schat zelf in wanneer uitstel gaat knellen: een investeerder die vijf dagen wacht is rood, een leverancier die twee dagen wacht niet. Zwaar onderwerp of belangrijke afzender → eerder rood. Maar: uitstel is bij David soms strategie, geen achterstand. Heeft hij een item bewust geparkeerd, of laat het leerlog zien dat hij dit sóórt zaken structureel bewust laat liggen (bijv. offertes tot het eind van de week), behandel het dan als geparkeerd — zichtbaar op de radar met reden, niet rood bovenaan. Vraag bij twijfel niet, maar noteer de aanname op het dashboard ("geparkeerd verondersteld — klopt dat?").
4. **Agenda-koppeling** — alles wat nodig is voor een afspraak van vandaag of morgen schuift automatisch omhoog.

Geef elk prioriteitsitem één zin **waarom nu** ("Verhuurder Grand Canal wacht 4 dagen op reactie over indexatie — afspraak staat morgen 10:00"). Gesnoozde items overslaan tot hun datum; afgevinkte items niet meer tonen.

## Voorbereid werk per item

Prioriteiten zonder voorzet zijn een to-do-lijst; de PA-waarde zit in het voorwerk. Per prioriteitsitem, waar van toepassing:

- **Concept-antwoord** — voor mails die om antwoord vragen: een verzendklaar concept in Davids stijl (Nederlands, kort, direct, vriendelijk-zakelijk, geen wollige beleefdheidsframes). Zet het concept inklapbaar onder het item. Als er een `my-writing-style`-profiel beschikbaar is, gebruik dat.
- **Oplossingsrichtingen** — bij knelpunten of beslissingen zonder eenduidig antwoord: 2–3 richtingen, elk met één regel voordeel en één regel nadeel, plus welke jij zou kiezen en waarom. Geen richtingen verzinnen bij items waar gewoon één logische actie is.
- **Vergaderbriefing** — per agenda-afspraak van vandaag en morgen: wie, waarover, relevante recente mails/berichten over dit onderwerp, en wat David moet weten of beslissen. Twee tot vijf regels; een intern uurtje heeft minder nodig dan een verhuurdersgesprek.

## Dashboard bouwen en publiceren

Bouw de pagina op basis van `assets/template.html` (mobile-first, geen externe dependencies). Secties in vaste volgorde:

1. **Kop** — datum/tijd van deze run + bronstatuschips
2. **Prioriteiten** — de gewogen lijst, rood/oranje/grijs, met "waarom nu", inklapbaar voorwerk en actieknoppen (✓ afgerond / ⏸ parkeer)
3. **Vandaag & morgen** — agenda-items met briefing per afspraak
4. **Radar** — langer lopende en bewust geparkeerde zaken (uitstel-teller en parkeer-reden zichtbaar)
5. **Vragen van je PA** — alleen tonen als er iets is: onvindbare afrondingen, aannames die bevestiging vragen
6. **Weekvoorstellen** — alleen in de week na een weekreview: de panelvoorstellen, kort
7. **Voet** — aantal verwerkte berichten per bron, link "ververs: vraag Claude"

Versleutel en publiceer daarna volgens `references/publicatie.md`. Het webadres verandert nooit; David heeft het als app op zijn beginscherm.

## Interactie tussen runs door

David reageert op twee manieren: via de chat, en via de actieknoppen op het dashboard zelf.

**Chat** — interpreteer ruim:

- "vink de factuur van X af" / "X is afgerond" → item op `afgerond`, start de leerlus (zie `references/leren.md`)
- "snooze de indexatie tot maandag" → `gesnoozed tot <datum>`; "dat laat ik bewust nog even liggen" → `bewust geparkeerd` mét de reden
- "voeg Roderik toe aan mijn VIP's" → config.json bijwerken
- "ververs mijn dashboard" → volledige run
- "zet erop dat ik Armanda moet bellen" → handmatig item toevoegen aan state.json met bron `handmatig`

**Dashboardknoppen** — elk prioriteits- en radaritem heeft knoppen "✓ afgerond" en "⏸ parkeer". Dat zijn mailto-links naar Davids eigen Gmail met onderwerp `PA afgerond: <item-id> <titel>` resp. `PA parkeer: <item-id> <titel>` — één tik op zijn telefoon en de mail staat klaar om te verzenden. Elke run zoekt in Gmail naar deze commandomails (onderwerp begint met "PA "), verwerkt ze (status bijwerken + leerlus bij afgerond), en filtert ze uit de prioriteiten. Zo werkt het dashboard als app, ook zonder chat.

Na elke mutatie: state/config wegschrijven én de pagina opnieuw publiceren, anders kijkt David op mobiel naar verouderde informatie.

## Leren van David

Dit dashboard wordt beter naarmate het David beter kent. Bij elk item dat op `afgerond` gaat: zoek in mail en WhatsApp na hóe hij het afrondde en schrijf de les naar `leerlog.md`. Kun je geen afronding vinden, zet dan een korte vraag in het blok "Vragen van je PA" op het dashboard. Wekelijks kijkt een expertpanel (psycholoog, gedragsanalist, ervaren PA, directiesecretaresse, NLP-trainer, life/business-coach — géén financiers) naar het leerlog en de gebruikshistorie en doet maximaal 5 voorstellen voor Davids efficiëntie. Het hele mechanisme staat in `references/leren.md` — lees dat bij afrondingen en bij de weekreview.

## Geplande runs (onbeheerd)

Een run die uit de uurplanning komt draait zonder David erbij. Stel dan géén vragen: bronnen die wegvallen krijgen een cache-chip, twijfelgevallen krijgen een voorzichtige inschatting met een korte kanttekening op het dashboard zelf. Verstuur nooit zelfstandig mail — concepten blijven concepten tot David ze zelf verstuurt of er expliciet in de chat om vraagt.

Houd geplande runs zuinig: geen diepe research per item, geen her-analyse van items die sinds de vorige run niet veranderd zijn (hergebruik de teksten uit de vorige state waar niets wijzigde).
