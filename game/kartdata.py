# All kode relatert til kartfunksjonen i spillet.
import engine as en

# Variabel med alle posisjonene for rommene
romposisjoner = {
    # Første kjelleretasje
    "rom1":  {"pos": (8, 4), "trapper": False},
    "rom2":  {"pos": (8, 8), "trapper": False},
    "rom3":  {"pos": (6, 8), "trapper": False},
    "rom4":  {"pos": (6, 4), "trapper": True},
    "rom5":  {"pos": (2, 16), "trapper": False},
    "rom6":  {"pos": (2, 0), "trapper": False},
    "rom7":  {"pos": (6, 16), "trapper": False},
    "rom8":  {"pos": (6, 0), "trapper": False},
    "rom9":  {"pos": (0, 0), "trapper": False},
    "rom10": {"pos": (2, 20), "trapper": False},
    "rom11": {"pos": (8, 0), "trapper": True},
    "gang1": {"pos": (4, 8), "trapper": False},
}

# Kart for første etasje (rom1–rom11 + gang1)

kart_etasje1 = " "

def vis_kart():
    # Nåværende rom og besøkt-dict hentes fra engine.py
    nåværende_rom = en.rom
    besøkt = en.besøkt

    # Lag tomt kart med riktig antall rader og kolonner
    rader = 9
    kolonner = 24
    kart_karakterer = [[" "]*kolonner for _ in range(rader)]

    # Rom som skal tegnes
    synlige_rom = [rom for rom, _ in romposisjoner.items() if besøkt.get(rom, False) or rom == nåværende_rom]

    # Tegn rom
    for rom in synlige_rom:
        row, col = romposisjoner[rom]["pos"]
        trapper = romposisjoner[rom].get("trapper", False)

        if rom == nåværende_rom:
            symbol = "[x]"
        elif trapper:
            symbol = "[⇅]"
        else:
            symbol = "[ ]"

        # Spesialhåndtering hubben (bred)
        if rom == "gang1":
            start = col - 8  # midten på 'g' som pos = 8
            for i, s in enumerate("[        g        ]"):
                kart_karakterer[row][start+i] = s
        else:
            kart_karakterer[row][col:col+3] = list(symbol)

    # Koblinger mellom rom
    koblinger = [
        ("rom1", "rom2"), ("rom2", "rom3"), ("rom3", "rom4"),
        ("rom3", "gang1"), ("gang1", "rom5"), ("gang1", "rom6"),
        ("gang1", "rom7"), ("gang1", "rom8"), ("rom5", "rom10"),
        ("rom6", "rom9"), ("rom8", "rom11"), ("rom8", "rom4")
    ]

    for a, b in koblinger:
        if a in synlige_rom and b in synlige_rom:
            row_a, col_a = romposisjoner[a]["pos"]
            row_b, col_b = romposisjoner[b]["pos"]

            # horisontal kobling
            if row_a == row_b:
                for c in range(min(col_a, col_b)+3, max(col_a, col_b)):
                    kart_karakterer[row_a][c] = "-"
            # vertikal kobling
            elif col_a == col_b:
                for r in range(min(row_a, row_b)+1, max(row_a, row_b)):
                    kart_karakterer[r][col_a+1] = "|"

    # Print kartet
    for line in kart_karakterer:
        print("".join(line))
