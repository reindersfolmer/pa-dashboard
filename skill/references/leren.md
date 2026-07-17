# Leren en weekreview

Het dashboard is geen statische takenlijst maar een PA die David leert kennen. Twee mechanismen: de afrond-leerlus (per item) en de weekreview (per week).

## De afrond-leerlus

Trigger: een item gaat op `afgerond` — via chat, via een "PA afgerond:"-commandomail in Gmail, of doordat een run zelf ziet dat de zaak beantwoord/opgelost is.

1. **Begin bij Davids eigen uitleg, als die er is.** De afgerond-knop vraagt hem in de mailbody "wat heb je gedaan?". Staat daar een antwoord, dan is dát het vertrekpunt: verifieer het in de relevante mailthread en WhatsApp (klopt het beeld, zit er meer detail in — bedrag, toon, doorlooptijd?) en verrijk de les ermee. Vind je géén spoor in de kanalen, log de les dan tóch op basis van zijn uitleg, met de aantekening "op Davids woord (bijv. telefonisch/persoonlijk afgehandeld)" — telefonisch afronden laat nu eenmaal geen thread achter, en dat is zelf ook een patroon dat het onthouden waard is. Stel in dat geval géén vraag meer; hij heeft het al verteld.
2. **Geen uitleg meegegeven?** Reconstrueer de afronding zelf: zoek in de relevante mailthread (Excite/Gmail, Urban via cache of Chrome) en WhatsApp hoe David het heeft afgehandeld: wat was zijn antwoord of actie, hoe snel, welke toon, delegeerde hij, belde hij in plaats van mailen, welk bedrag of compromis kwam eruit?
3. **Vind je een afronding** (of heb je Davids uitleg): schrijf één compacte les naar `/PA Dashboard/leerlog.md`, gedateerd, in dit format:
   ```
   ## 2026-07-16 — Schadeclaim kamer 12 (gast)
   Afgerond: tegenbod €450 i.p.v. gevraagde €900, telefonisch, binnen 1 dag na escalatie.
   Patroon: bij gastclaims doet David snel een telefonisch tegenbod rond 50%.
   ```
4. **Vind je géén afronding én gaf David geen uitleg**: niet gissen. Zet een korte vraag in het dashboardblok "Vragen van je PA" ("Hoe is de schadeclaim van kamer 12 afgelopen? Ik vind geen antwoord in mail of WhatsApp."). Beantwoordt David hem, dan alsnog de les loggen; negeert hij hem twee weken, dan de vraag stil laten vervallen.

**Bewust uitstel is ook een les.** Parkeert David iets expliciet ("laat maar even liggen, ik wacht op de jaarcijfers"), log dan het patroon. Zie je drie keer hetzelfde soort item bewust geparkeerd worden, dan is dat een regel: dit type niet meer rood maken, wel op de radar houden.

**Het leerlog gebruiken.** Lees leerlog.md bij elke run (het is klein; houd het klein — maximaal ~60 lessen, oudste patronen samenvoegen tot algemene regels). Pas het toe op twee plekken: prioritering (wat David bewust laat liggen niet opdringen) en voorwerk (concepten en oplossingsrichtingen schrijven zoals David het de vorige keren daadwerkelijk aanpakte — zijn tegenbod-stijl, zijn toon per relatietype, zijn voorkeur voor bellen boven lange mails waar dat bleek).

## De weekreview

Eén keer per week (aparte geplande run, vrijdag 16:00) — niet in de uur-runs.

1. Verzamel de week: run_log, leerlog-lessen van deze week, wat David afvinkte/parkeerde/negeerde, welke dashboardonderdelen hij gebruikte of juist nooit aanraakt, doorlooptijden van items.
2. Roep de skill `expert-panel-review` aan op die weeksamenvatting, met een afwijkend panel — géén financiers of investeerders, wel: een psycholoog, een gedragsanalist, een doorgewinterde executive PA, een directiesecretaresse, een NLP-trainer en een life/business-coach. Vraagstelling aan het panel: "Hoe kan David komende week efficiënter en met minder kop-ruimte werken, en hoe kan zijn PA-dashboard hem daar beter bij helpen?"
3. Sla de volledige review (alle panelreviews + CEO-synthese) op als Google-document in Davids Drive-map "PA Dashboard" (mcp__Google_Drive__create_file, titel "Weekreview N — <datum>"), zodat hij hem kan teruglezen. Schrijf de CEO-synthese (max 5 punten) daarnaast naar `/PA Dashboard/weekvoorstellen.json` (klein los bestand: {datum, voorstellen[]}) — elke run neemt dat blok over op het dashboard tot de volgende review het vervangt. De voorstellen komen als blok **Weekvoorstellen** op het dashboard, elk voorstel in één of twee zinnen, concreet ("verplaats je mailmoment naar 11:00 — je beantwoordt 's ochtends vooral reactief" — niet "verbeter je time-management"). Voorstellen over het dashboard zelf ("de radar wordt nooit geopend, zal ik hem inkorten?") mag het panel ook doen; voer die pas uit als David akkoord geeft.
4. Log in leerlog.md welke voorstellen David overneemt of afwijst — ook dát is een patroon.

De weekreview is onbeheerd: geen vragen stellen, alleen voorstellen op het dashboard zetten. David reageert via chat als iets hem aanspreekt.
