# Kjellerbeistet

**Forfatter:** AnBasement  
**Versjon:** 1.0.2  
**Lisens:** GNU GPLv3

---

## Om prosjektet

*Kjellerbeistet* er et tekstbasert eventyrspill skrevet i Python.
Spilleren navigerer gjennom flere rom i en mørk kjeller, unngår det fryktede Kjellerbeistet, og prøver å finne veien ut ved hjelp av observasjon, gjenstander og valg.

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

---

## Plan for videre utvikling

### Uke 4

- Implementere dictionaries for å lagre romtilstander og mulige valg mer dynamisk
- Lage funksjoner for å håndtere spill-logikk som overgang mellom rom og håndtering av gjenstander
- Innføre feilhåndtering for brukerinput for å gjøre spillet mer robust
- Utvide historien med nye valg, rom og grener for mer dybde og variasjon

---

## Hvordan kjøre spillet

1. Sørg for at Python 3 er installert på din maskin
2. Last ned filen `eventyr.py`
3. Kjør programmet fra terminalen med kommandoen:

```bash
python eventyr.py
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
