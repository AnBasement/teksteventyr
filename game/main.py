###############################################################################
# eventyr.py
#
# Forfatter: AnBasement
# Versjon: 1.5.1
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
import inspect

# Dictionary for håndtering av romfunksjoner
romfunksjoner = {
    "rom1": rooms.rom1,
    "rom2": rooms.rom2,
    "rom3": rooms.rom3,
    "rom4": rooms.rom4,
    "gang1": rooms.gang1,
    "rom5": rooms.rom5,
    "rom6": rooms.rom6,
    "rom7": rooms.rom7,
    "rom8": rooms.rom8,
    "rom9": rooms.rom9,
    "rom10": rooms.rom10,
    "rom11": rooms.rom11,
    "rom12": rooms.rom12,
    "rom13": rooms.rom13,
    "kjeller2_1": rooms.kjeller2_1,
    "kjeller2_2": rooms.kjeller2_2,
    "kjeller2_3": rooms.kjeller2_3,
    "kjeller2_4": rooms.kjeller2_4,
    "kjeller2_5": rooms.kjeller2_5
}

# Håndtering av rom for hovedløkken
def håndter_rom(spilltilstand):
    """
    Kaller riktig romfunksjon basert på nåværende rom.

    Args:
        rom (str): Navnet på det nåværende rommet.

    Returns:
        tuple: Oppdatert rom, restart-flag, status-dict, besøkt-dict.
    """
    rom = spilltilstand["rom"]
    if rom not in romfunksjoner:
        print(f"Feil: Rom '{rom}' finnes ikke!")
        return spilltilstand

    engine.sett_spilltilstand(spilltilstand)

    oppdatert_tilstand = romfunksjoner[rom](spilltilstand)

    engine.sett_spilltilstand(oppdatert_tilstand)

    return oppdatert_tilstand


def main():
    """
    Main game loop and initialization.
    """
    print("""Velkommen til det tekstbaserte eventyret 'Kjellerbeistet'!
    Du må forsøke å navigere deg til trappen og ut av kjelleren uten å støte på beistet.
    Om du trenger hjelp kan du skrive 'hjelp' for en liste over godkjette kommandoer.""")

    # Initialiseringsvariabler
    spilltilstand = engine.hent_spilltilstand()
    avslutt = False

    # Start eller last inn spill
    while True:
        start = input('Skriv "start" for å begynne, eller "last inn" for å laste inn et tidligere spill.\n> ').strip().lower()
        if start == "start":
            break
        elif start == "last inn":
            loaded_state = engine.last_inn_spill()
            if loaded_state:
                spilltilstand = loaded_state
            break
        print(engine.ugyldig)

    # Hovedløkke
    try:
        while not avslutt:
            spilltilstand = håndter_rom(spilltilstand)
            
            if spilltilstand["restart"]:
                # Reset game state
                spilltilstand = {
                    "rom": "rom1",
                    "restart": False,
                    "besøkt": {rom: False for rom in engine.besøkt},
                    "status": {key: False for key in engine.status},
                    "inventar": {item: False for item in engine.inventar}
                }
                
    except KeyboardInterrupt:
        print("\n\nSpillet ble avbrutt av bruker.")
        save_choice = input("Vil du lagre spillet før du avslutter? (ja/nei): ")
        if save_choice.lower() == "ja":
            engine.lagre_spill()
        print("Takk for at du spilte!")
        
    except Exception as e:
        print(f"\nEn uventet feil oppstod: {e}")
        print("Forsøker å lagre spillet...")
        try:
            engine.lagre_spill()
            print("Spillet ble lagret.")
        except:
            print("Kunne ikke lagre spillet.")
        raise

if __name__ == "__main__":
    main()