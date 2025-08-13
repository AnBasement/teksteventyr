# Changelog

Alle endringer gjort på eventyr.py vil dokumenteres her.

Formatert etter [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

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