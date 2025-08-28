###############################################################################
# eventyr.py
#
# Forfatter: AnBasement
# Versjon: 1.2.2
#
# Beskrivelse:
#   Et tekstbasert eventyrspill hvor spilleren navigerer gjennom flere rom
#   og unngår beistet som holder til der.
#
# Lisens:
#   Dette programmet er lisensiert under GNU General Public License v3.0 (GPLv3).
#   Du kan distribuere og endre det under vilkårene i GPLv3.
#   Se https://www.gnu.org/licenses/gpl-3.0.html for full lisensinformasjon.
###############################################################################

# Programmet er skrevet som en del av et kurs for å lære python.
# Jeg bruker det også for å lære litt om hvordan GitHub fungerer,
# og vil derfor bruke issues og pull requests.
# For senere oppdateringer, fikse boolske sjekker, bruke dict

import rooms
import engine

print("""Velkommen til det tekstbaserte eventyret 'Kjellerbeistet'!
Du må forsøke å navigere deg til trappen og ut av kjelleren uten å støte på beistet.
Om du trenger hjelp kan du skrive 'hjelp' for en liste over godkjente kommandoer.""")

# Krever at spiller skriver "start" for å begynne
while True:
    start = input('Skriv "start" for å begynne, eller "last inn" for å laste inn et tidligere spill. ').strip().lower()
    if start == "start":
        break
    elif start == "last inn":
        besøkt, status, rom = engine.last_inn_spill()
        break
    print(engine.ugyldig)
    
# Begynner spillet
while True:
    if engine.restart:
        rom = "rom1"
        for rom_navn in besøkt:
            besøkt[rom_navn] = False
    
        # Nullstill status
        for key in status:
            status[key] = False
    
    engine.restart = False

    # Hovedløkke for å navigere gjennom rommene
    if engine.rom == "rom1":
        rom, restart, besøkt = rooms.rom1(engine.rom, engine.restart, engine.besøkt)
    elif engine.rom == "rom2":
        rom, restart, status, besøkt = rooms.rom2(engine.rom, engine.restart, status, engine.besøkt)
    elif engine.rom == "rom3":
        rom, restart, status, besøkt = rooms.rom3(engine.rom, engine.restart, status, engine.besøkt)
    elif engine.rom == "rom4":
        rom, restart, status, besøkt = rooms.rom4(engine.rom, engine.restart, status, engine.besøkt)
    elif engine.rom == "gang1":
        rom, restart, status, besøkt = rooms.gang1(engine.rom, engine.restart, status, engine.besøkt)
    elif engine.rom == "rom5":
        rom, restart, status, besøkt = rooms.rom5(engine.rom, engine.restart, status, engine.besøkt)
    elif engine.rom == "rom6":
        rom, restart, status, besøkt = rooms.rom6(engine.rom, engine.restart, status, engine.besøkt)
    elif engine.rom == "rom7":
        rom, restart, status, besøkt = rooms.rom7(engine.rom, engine.restart, status, engine.besøkt)
    elif engine.rom == "rom8":
        rom, restart, status, besøkt = rooms.rom8(engine.rom, engine.restart, status, engine.besøkt)