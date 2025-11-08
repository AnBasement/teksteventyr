# All kode relatert til kartfunksjonen i spillet.
import engine as en

# Dict med alle posisjonene for rommene i hovedetasjen
romposisjoner = {
    "rom1":  {"pos": (8, 8), "trapper": False},
    "rom2":  {"pos": (8, 12), "trapper": False},
    "rom3":  {"pos": (6, 12), "trapper": False},
    "rom4":  {"pos": (6, 8), "trapper": True},
    "rom5":  {"pos": (2, 20), "trapper": False},
    "rom6":  {"pos": (2, 4), "trapper": False},
    "rom7":  {"pos": (6, 20), "trapper": False},
    "rom8":  {"pos": (6, 4), "trapper": False},
    "rom9":  {"pos": (0, 4), "trapper": False},
    "rom10": {"pos": (2, 24), "trapper": False},
    "rom11": {"pos": (8, 4), "trapper": True},
    "gang1": {"pos": (4, 12), "trapper": False},
    "rom12": {"pos": (8, 0), "trapper": False},
    "rom13": {"pos": (10, 0), "trapper": False},
}

# Dict med alle posisjonene for rommene i kjeller2
kjeller2_posisjoner = {
    "kjeller2_1": {"pos": (2, 4), "trapper": True},
    "kjeller2_2": {"pos": (2, 8), "trapper": False},
    "kjeller2_3": {"pos": (4, 4), "trapper": False},
    "kjeller2_4": {"pos": (2, 0), "trapper": False},
    "kjeller2_5": {"pos": (0, 4), "trapper": False}
}

# Basis-offset for hvert kart. Øk kolonneverdien for å flytte hele kartet mot
# høyre for å få plass til nye rom på venstresiden, eller radverdien for
# å flytte kartet nedover uten å endre hver enkelt oppføring.
ETASJE_OFFSETS = {
    "etasje1": (0, 0),
    "kjeller2": (0, 0),
}


def hent_posisjon(romdata, offset):
    """
    Returnerer absolutt (rad, kolonne) for et rom. Hvis rommet definerer
    'pos_rel', kombineres den med offseten slik at vi kan flytte hele kartet
    uten å oppdatere hver koordinat.
    """
    if "pos" in romdata:
        return romdata["pos"]

    rel_rad, rel_kol = romdata.get("pos_rel", (0, 0))
    off_rad, off_kol = offset
    return rel_rad + off_rad, rel_kol + off_kol


def vis_kart():
    # Nåværende rom og besøkt-dict hentes fra engine.py
    nåværende_rom = en.rom
    besøkt = en.besøkt

    # Automatisk velg etasje basert på hvilket rom spilleren er i
    if nåværende_rom in romposisjoner:
        rompos = romposisjoner
        rader, kolonner = 11, 28
        offset = ETASJE_OFFSETS["etasje1"]
        koblinger = [
            ("rom1", "rom2"), ("rom2", "rom3"), ("rom3", "rom4"),
            ("rom3", "gang1"), ("gang1", "rom5"), ("gang1", "rom6"),
            ("gang1", "rom7"), ("gang1", "rom8"), ("rom5", "rom10"),
            ("rom6", "rom9"), ("rom8", "rom11"), ("rom8", "rom4"),
            ("rom10", "rom12"), ("rom11", "rom12"), ("rom12", "rom13")
        ]
    elif nåværende_rom in kjeller2_posisjoner:
        rompos = kjeller2_posisjoner
        rader, kolonner = 5, 20
        offset = ETASJE_OFFSETS["kjeller2"]
        koblinger = [
            ("kjeller2_1", "kjeller2_2"), ("kjeller2_1", "kjeller2_3"), ("kjeller2_1", "kjeller2_4"),
            ("kjeller2_1", "kjeller2_5")
        ]
    else:
        print("Ingen kartdata for dette rommet.")
        return

    # Lag tomt kart
    kart_karakterer = [[" "]*kolonner for _ in range(rader)]

    # Rom som skal tegnes
    synlige_rom = [rom for rom, _ in rompos.items() if besøkt.get(rom, False) or rom == nåværende_rom]

    # Tegn rom
    for rom in synlige_rom:
        row, col = hent_posisjon(rompos[rom], offset)
        trapper = rompos[rom].get("trapper", False)
        if rom == nåværende_rom:
            symbol = "[x]"
        elif trapper:
            symbol = "[⇅]"
        else:
            symbol = "[ ]"
        kart_karakterer[row][col:col+3] = list(symbol)

    # Tegn koblinger
    for a, b in koblinger:
        if a in synlige_rom and b in synlige_rom:
            row_a, col_a = hent_posisjon(rompos[a], offset)
            row_b, col_b = hent_posisjon(rompos[b], offset)

            if row_a == row_b:
                for c in range(min(col_a, col_b)+3, max(col_a, col_b)):
                    kart_karakterer[row_a][c] = "-"
            elif col_a == col_b:
                for r in range(min(row_a, row_b)+1, max(row_a, row_b)):
                    kart_karakterer[r][col_a+1] = "|"
            else:
                mid_col = col_b + 1

                if mid_col > col_a:
                    start = col_a + 3
                    for c in range(start, mid_col + 1):
                        kart_karakterer[row_a][c] = "-"
                else:
                    start = col_a - 1
                    for c in range(start, mid_col - 1, -1):
                        kart_karakterer[row_a][c] = "-"

                step = 1 if row_b > row_a else -1
                for r in range(row_a + step, row_b, step):
                    kart_karakterer[r][mid_col] = "|"

    # Print kartet
    for line in kart_karakterer:
        print("".join(line))
