# Changelog

Alle endringer gjort på eventyr.py vil dokumenteres her.

Formatert etter [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

---

## [1.3.0] - 2025-08-30
### Lagt til
- Tre nye rom er introdusert.
    - Soppkrypten, et lite rom som nås via en dør i rom 6.
    - Arkivrommet, et arkivrom som nås fra en skjult dør bak hyller i rom 5.
    - Lukerommet, nås via en dør på sørveggen i rom 8.

### Fikset
- Bruk av kommandoen utforsk i rom 8 oppdateres nå korrekt etter at ventilen blir åpnet.

---

## [1.2.3] - 2025-08-29
### Endret
- Eventyr.py er splittet opp i tre filer for bedre oversikt.
    - main.py inneholder hovedløkken for spillet.
    - rooms.py inneholder funksjonene for de individuelle rommene.
    - engine.py inneholder hjelpefunksjoner/utilities.
- Bruker nå os-modulen for å sikre lagring av spill til samme mappe som main.py

### Fikset
- Fikset interaksjon med skap i rom 2.
- Fikset gyldige ord i rom 5 for esker og reoler.
- Gjort det mulig å faktisk komme seg inn i rom 7 og 8 fra gang 1.
- Lagt til flere gyldige ord i rom 7 og 8.
- Fikset ventil og oljeovn i rom 8 for å unngå en evig print-løkke.
- Fikset oppdatering av status for oljekanner i rom 8.
- Dersom spiller forsøker å laste inn et lagret spill uten at det finnes en savegame.txt vil spillet heller nå startes automatisk.

---

## [1.2.2] - 2025-08-27
### Lagt til
- Mulighet for å lagre og laste inn spillstatus.

### Fikset
- Fikset en TypeError om spiller valgte nei i rom2_ost.

---

## [1.2.1] - 2025-08-21
### Fikset
- Fikset en print-melding i rom 8 som skulle printet variabelen "ugyldig", men heller printet ordet "ugyldig."
- Inkluderte "fermenteringsbeholder" i gyldige ord for rom 7.

---

## [1.2.0] - 2025-08-21
### Lagt til
- Legger til rom 7 og 8.

### Endret
- Endrer utforsk i rom 4 til å sjekke status avhengig av spillers handlinger i rom 8.
- Endrer trapp i rom 4 til å sjekke status avhengig av spillers handlinger i rom 8.

---

## [1.1.1] - 2025-08-16
### Lagt til
- Funksjon "tallkode", som lar bruker skrive inn "tallkode" for å få en påminnelse på tallene de har funnet.

### Endret
- Lar spiller forsøke kodelåsen så mange ganger de vil, eller skrive "avbryt" for å gå tilbake til rommet.
- Endrer romnavn for rom6 og 7 til rom5 og rom6 ettersom rom5 ble endret til gang1 før v1.1.0.
- Oppdaterer hjelp-kommandoen til å inkludere den nye kommandoen.
- Oppdaterer utforsk_tekst for rom5 og rom6 til å inkludere dør.
- Rydder i hvordan programmet håndterer utforsk_tekst og inngang_tekst.
- Rydder i hvordan programmet håndterer en restart slik at spiller alltid plasseres i rom1 og besøkt settes til False.

---

## [1.1.0] - 2025-08-16
### Lagt til
- Lagt til gang1, rom6 og rom7.

### Endret
- Har introdusert en kode spilleren må bruke for å få tak i brekkjern. Endret i den sammenheng hvordan skrivebordet i rom4 virker, og en beskrivelse tidligere i spillet.

---

## [1.0.2] - 2025-08-13
### Endret
- Tatt i bruk funksjoner for en rekke hendelser:
    - Flyttet rom3 til en egen funksjon som kan calles i hovedløkken
        - Flyttet malingsspann i rom3 til egen funksjon
    - Flyttet rom4 til en egen funksjon som kan calles i hovedløkken
        - Flyttet trapp i rom4 til egen funksjon
        - Flyttet skrivebord i rom4 til egen funksjon
    - Flyttet "hjelp" og "utforsk" i en funksjon slik at det ikke må skrives ut i funksjonen for hvert rom
    - Pakket tap inn i en funksjon som brukes to steder

### Fikset
- Omstart etter fullført spill sender nå spiller tilbake til rom1 og printer utforsk-melding.

---

## [1.0.1] - 2025-08-12
### Endret
- Tatt i bruk funksjoner for en rekke hendelser:
    - Laget en funksjon som fanger opp første gang spiller besøker rom og endrer tekst som printes basert på dette.
    - Flyttet rom1 til en egen funksjon som kan calles i hovedløkken
    - Flyttet rom2 til en egen funksjon som kan calles i hovedløkken
        - Flyttet arbeidsbenken i rom2 til egen funksjon
        - Flyttet valget øst i rom2 til egen funksjon

---

## [1.0.0] - 2025-08-11
### Lagt til
- Legger til rom3 og rom4.
- Ferdigstiller første versjon av spillet.

### Endret
- Renskriving av teksten i "hjelp"-kommandoen for å teste issues/pull requests.
- Endre kommentar på slutten av while-løkke for rom 2.

---

## [0.1.1] - 2025-08-10
### Lagt til
- Interagerbare gjenstander i rommene.
- Flavors.
- Kommandoer for "hjelp" og "utforsk" om spiller sitter fast.

### Endret
- Gått bort fra overdreven bruk av nestede while-løkker.

### Fjernet
- Fjernet rom 3 for å fokusere mer på utvidelse av rom 1 og 2.

---

## [Upublisert] - 2025-08-08 - 2025-08-09

### Lagt til
- Prototype for et tekstbasert eventyrspill.
- Tre rom med med mulighet for å bevege mellom dem.
- Bruk av while-løkker for spillervalg.