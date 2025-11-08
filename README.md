# Kjellerbeistet

**Forfatter:** AnBasement  
**Versjon:** 1.5.1  
**Lisens:** GNU GPLv3

---

## Om prosjektet

*Kjellerbeistet* er et tekstbasert eventyrspill skrevet i Python.
Spilleren navigerer gjennom flere rom i en mørk kjeller, unngår det fryktede Kjellerbeistet, og prøver å finne veien ut ved hjelp av observasjon, interagerbare objekter og gjenstander, og valg.

Dette prosjektet er både et morsomt lite spill og et læringsprosjekt for å bli bedre i Python-programmering, samt å bli kjent med GitHub-arbeidsflyten med issues og pull requests.

---

## Status

- Påbegynt i uke 2 av læringsløpet mitt i Python
- Grunnleggende spillmekanikk på plass:
  - Navigasjon mellom rom med kommandoer basert på himmelretninger
  - Enkle objekter som kan plukkes opp og brukes
  - Restart-mulighet ved tap
- Klar for testing og enkel utvidelse
- Koden inneholder mange kommentarer og bruker variabler for enkel endring

- Per uke 3 er rommene flyttet til funksjoner slik at hovedløkken for spillet er enkel
  - Utvalgte interagerbare objekter er også flyttet inn i funksjoner
- Bruker nå dicts for sjekk av status på interagerbare objekter og gyldige valg

- Per uke 4 er tre rom lagt til for totalt 7, med et ekstra puslespill spilleren må løse for å komme seg ut av kjelleren.

- I uke fem ble to nye rom lagt til for totalt 9, inkludert endringer til rom 4.

- Muligheten for å lagre og fortsette spillet ble lagt til i uke 6.

- Filen ble delt opp i tre i uke 7 for bedre oversikt. Også en rekke bugfikser og bruk av os-modul for enklere kontroll over filstier. Tre nye rom ble introdusert som setter opp for videre utvidelse. Innfører også et inventar og endrer kommando-bruk.

- Poengsystem, ASCII-kart og en sjansemekanikk er blitt introdusert sammen med utvidelse til et nytt nivå. Spillet lagres til JSON istedenfor en txt-fil.

---

## Plan for videre utvikling

- Både forenkle videre utvidelser og kutte ned på antall linjer med kode ved å gjøre rom om til klasser.

---

## Hvordan kjøre spillet

1. Sørg for at Python 3 er installert på din maskin
2. Last ned filene i mappen 'game':  `main.py`, `rooms.py` og `engine.py`
3. Kjør programmet fra terminalen med kommandoen:

    ```bash
    python main.py
    ```

4. Følg instruksjonene i spillet

---

## Bidra

Prosjektet er åpent for forbedringer og nye idéer.
Bruk gjerne GitHubs issue- og pull request-system for å komme med forslag eller feilrettinger.

---

## Lisens

Dette programmet er lisensiert under GNU General Public License v3.0 (GPLv3).
Se [https://www.gnu.org/licenses/gpl-3.0.html](https://www.gnu.org/licenses/gpl-3.0.html) for detaljer.
