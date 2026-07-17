# Bronnen uitlezen

Per bron: hoe je hem uitleest, wat je eruit haalt, en wat je doet als hij niet bereikbaar is. Lees connector-bronnen parallel uit waar dat kan. Doel per bron: genoeg om te prioriteren — geen volledige archieven binnenhalen.

## Overzicht

| Bron | Route | Bereikbaar in geplande runs? |
|---|---|---|
| Excite 365 mail | `mcp__Microsoft_365__outlook_email_search` | ja |
| Excite 365 agenda | `mcp__Microsoft_365__outlook_calendar_search` | ja |
| Gmail | `mcp__Gmail__search_threads` / `get_thread` | ja |
| Dropbox (config/state) | `mcp__Dropbox__*` | ja |
| Urban 365 mail | Chrome → outlook.office.com | alleen als Chrome openstaat |
| Urban 365 agenda | Chrome → outlook.office.com/calendar | alleen als Chrome openstaat |
| WhatsApp | Chrome → web.whatsapp.com | alleen als Chrome openstaat |
| Google-agenda | Chrome → calendar.google.com | alleen als Chrome openstaat |

## Excite 365 (david@excitehotels.nl)

- Mail: zoek ongelezen en recente berichten van de afgelopen 3 werkdagen, plus gemarkeerde/gevlagde mail. Haal per relevant bericht op: afzender, onderwerp, datum, kern van de inhoud, en of er een bedrag/deadline in staat.
- Agenda: alle afspraken van vandaag en morgen (en maandag als het vrijdag is), met deelnemers en omschrijving.

## Gmail (reindersfolmer@gmail.com)

Zoek threads van de afgelopen 3 werkdagen plus alles met een ster. Gmail is Davids privé/overloop-kanaal: filter nieuwsbrieven en notificaties er hard uit; alleen mail van mensen telt.

Zoek daarnaast expliciet naar **commandomails**: door David aan zichzelf gestuurde mails met onderwerp dat begint met `PA afgerond:`, `PA snooze:` of `PA parkeer:` (afkomstig van de dashboardknoppen). Zoek breed (`subject:"PA afgerond:" OR subject:"PA snooze:" OR subject:"PA parkeer:"`) — een Gmail-regel archiveert ze meteen onder het label **PA-dashboard**, dus ze staan meestal níet in de inbox; Gmail-search vindt ze toch. Lees ook de body — daar staat Davids toelichting (afgerond), de snooze-termijn of de parkeer-reden. Verwerk ze — status bijwerken, leerlus starten bij afgerond (zie `references/leren.md`) — en markeer ze daarna als verwerkt: geef de thread het label **PA-dashboard/verwerkt** (aanmaken als het nog niet bestaat) zodat een volgende run ze niet dubbel verwerkt. Neem alleen commandomails zónder dat label mee, en houd ze altijd buiten de prioriteitenlijst.

## Chrome-bronnen (Urban, WhatsApp, Google-agenda)

Check éérst één keer of Chrome bereikbaar is: laad de claude-in-chrome tools via ToolSearch (één call, kernset) en roep `tabs_context_mcp` aan. Faalt dat → alle vier de Chrome-bronnen op cache, niet per bron opnieuw proberen.

Werkwijze als Chrome wél bereikbaar is — maak per site een nieuw tabblad, en sluit je tabbladen na afloop:

- **Urban mail** — navigeer naar `https://outlook.office.com/mail/`. Als er een accountkeuze of login verschijnt: niet zelf inloggen; markeer de bron als "niet ingelogd" en meld het onderaan het dashboard. Lees anders de inbox-lijst (afzender, onderwerp, tijd) en open alleen berichten die er voor prioritering toe doen.
- **Urban agenda** — `https://outlook.office.com/calendar/view/week`, lees vandaag + morgen.
- **WhatsApp** — `https://web.whatsapp.com`. Meldt de pagina "WhatsApp is geopend in een ander venster", klik dan op "Hier gebruiken" (Davids andere venster moet daarna herladen — dat weet hij). Lees de chatlijst: chats met ongelezen-badge en chats met activiteit vandaag. Open alleen die chats en haal de recente berichten op. Negeer groepsgebabbel zonder vraag of actie voor David; een bericht telt als het een vraag, verzoek, bedrag of afspraak bevat. Privécontext die niets met werk te maken heeft hoort niet op het dashboard, tenzij het een afspraak of actie is.
- **Google-agenda** — `https://calendar.google.com`, dag/weekweergave, vandaag + morgen.

Schrijf van elke gelezen Chrome-bron een compacte snapshot naar `state.json → cache` met timestamp, zodat de eerstvolgende geplande run iets heeft om op terug te vallen.

## Cache-gedrag

Bij terugvallen op cache: gebruik de snapshot alsof het verse data is voor prioritering, maar toon de chip "cache van <tijd>" en behandel tijdgevoelige conclusies voorzichtig (geen "wacht al 5 dagen" beweren op basis van een snapshot van gisteren zonder dat te melden). Cache ouder dan 24 uur: toon de bron als **verouderd** en neem alleen items mee die toen al belangrijk waren.

## Uitstel-tracking

Elk mail-/berichtitem dat om actie van David vraagt krijgt bij eerste signalering een entry in `state.json → items` met `eerste_gezien`. Bij elke run: check of het item inmiddels beantwoord lijkt (antwoord in de thread, afspraak gepland) en zet het dan op `afgevinkt` — het dashboard moet zichzelf opruimen, niet alleen groeien.
