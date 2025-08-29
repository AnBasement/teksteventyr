# Inneholder alt av hjelpefunksjoner.

import os

# Variabel som definerer filstien
lagret_spill = os.path.join(os.path.dirname(__file__), "savegame.txt")

# Definerer variabler som blir brukt flere ganger
ugyldig = "Ugyldig svar, prøv igjen. "
omstart = "Vil du spille igjen? (ja/nei) "
tap = "Kjellerbeistet tok deg, og omverdenen hører aldri fra deg igjen."
spiller_prompt = "Hva vil du gjøre? "
hjelp = "Spillet liker bare ett-ords kommandoer – hold det enkelt!\nFor å bevege deg fra rom til rom kan du bruke himmelretningene (nord, sør, sørvest etc.).\nOm du har glemt hvor du er, kan du skrive 'utforsk' for en påminnelse, eller 'tallkode' for en påminnelse om koden! Du kan også skrive 'lagre' for å lagre fremgangen din."

# Variabel for rommet man befinner seg i. Begynner på "rom1" og endres avhengig av brukers valg.
rom = "rom1"

# Definerer variabelen "restart" som False
restart = False

# Lagre spillstatus
def lagre_spill(besøkt, status, rom):
    with open(lagret_spill, "w", encoding="utf-8") as fil:
        fil.write("#besøkt\n")
        for key, value in besøkt.items():
            fil.write(f"{key}={value}\n")
        fil.write("#status\n")
        for key, value in status.items():
            fil.write(f"{key}={value}\n")
        fil.write("#rom\n")
        fil.write(f"{rom}")
    print("Spillet ditt er lagret!")

# Laste inn spillstaturs
def last_inn_spill():
    global besøkt, status, rom 
    if not os.path.exists(lagret_spill):
        print("Finner ikke et lagret spill, starter et nytt!")
        return besøkt, status, rom
    with open(lagret_spill, "r", encoding="utf-8") as fil:
        seksjon = None
        for linje in fil:
            linje = linje.strip()
            if not linje or linje.startswith("#"):  # Skipper tomme linjer
                if linje == "#besøkt":
                    seksjon = "besøkt"
                elif linje == "#status":
                    seksjon = "status"
                elif linje == "#rom":
                    seksjon = "rom"
                continue

            if seksjon == "besøkt":
                key, value = linje.split("=")
                besøkt[key] = value == "True"
            elif seksjon == "status":
                key, value = linje.split("=")
                status[key] = value == "True"
            elif seksjon == "rom":
                rom = linje

    print("Velkommen tilbake!")
    return besøkt, status, rom

# Funksjon for å sjekke gyldige valg
def sjekk_gyldig_valg(prompt, gyldige_valg, ugyldig):
    while True:
        valg = input(prompt).strip().lower()
        if valg in gyldige_valg:
            return valg
        print(ugyldig)

# Variabler som kun brukes én gang i gjeldende rom, men ikke skal inkluderes i "utforsk"-kommando
rom1_inngang_tekst = ("")
rom2_inngang_tekst = (
    "Idet du går inn i det neste rommet smeller døren igjen bak deg.\n"
    "Du forsøker å åpne den igjen, men den sitter bom fast."
)
rom3_inngang_tekst = (
    "Du åpner forsiktig døren mot nord, og tar et stille steg inn i det nye rommet.\n"
    "Du trykker på en lysbryter ved siden av deg, og til din store overraskelse blir rommet godt opplyst av et par vegglamper."
)
rom4_inngang_tekst = (
    "Idet du går gjennom den tomme dørkarmen i vest, kjenner du frisk luft treffe deg i ansiktet."
)
gang1_inngang_tekst = (
    "Du prøver døren, som lett gir etter.\n"
    "Du blir møtt av en varm, tung og klam luft."
)
rom5_inngang_tekst = (
    "Døren har to separate låser, men idet du vrir om håndtaket gir den lett etter."
)
rom6_inngang_tekst = (
    "Det kommer en relativt sterk, men frisk lukt fra døren, som blir forklart idet du åpner den."
)
rom7_inngang_tekst = (
    "En søt lukt treffer deg i fleisen idet døren går opp, og du trer inn i et mykt opplyst rom."
)
rom8_inngang_tekst = (
    "Når du åpner døren føles det som om du åpner døren til en badstue idet varm luft strømmer ut i den forholdsvis kjølige gangen."
)

# Variabler som printes ved bruk av "utforsk"-kommandoen
rom1_utforsk_tekst = ("Du befinner deg i et mørkt rom med et lite, skittent vindu like under taket til vest med en stige under. Til øst er det en dør."
)

rom2_utforsk_tekst = (
    "En lyspære i taket gjør sitt beste for å lyse opp det mørke rommet, uten særlig hell.\n"
    "Du ser et skap i et hjørne, en arbeidsbenk, og dører til nord og øst."
)
rom3_utforsk_tekst = (
    "Rommet er fullt av skrot. Det står noen bokser i det ene hjørnet og bulkete og gamle malingsspann i et annet.\n"
    "Der er dører til sør og nord, og en åpning mot vest."
)
rom4_utforsk_tekst = (
    "I midten av rommet står en trapp opp til etasjen over. Du ser en dør i enden av trappen.\n" \
    "Under trappen står et gammelt skrivebord med en stol. På den ene veggen ser du en stor ventil.\n"
    "Der er en åpning på østveggen."
)
gang1_utforsk_tekst = (
    "Du står i en lang gang. Foran deg ser du to dører, en til nordvest og en til nordøst.\n" \
    "Gangen strekker seg fra vest til øst, og når du ser deg rundt ser du også dører til sørvest og sørøst.\n" \
    "Gangen er opplyst av spottere, og fremstår ellers som helt bar."
)
rom5_utforsk_tekst = (
    "Du finner deg omringet av høye stabler av kasser og esker. To høye reoler står midt i rommet, og langs den bakre veggen står et enkelt skap. En dør leder sør."
)
rom6_utforsk_tekst = (
    "Du står i noe som ligner på en vaskekjeller. Det står to oppvaskamaskiner stablet opp langs den ene veggen.\n" \
    "Den bakre veggen og taket er fullt av rør, noen med små lekkasjer og andre så rustne at det er et under de ikke lekker. På ett av rørene er det et stort rødt hjul.\n" \
    "Langs den siste veggen står en rekke hyller med forskjellige vaskemidler på. En dør leder sør."
)
rom7_utforsk_tekst = (
    "Rommet minner om en vinkjeller for en tenåringsgutt. Langs veggene ligger store plastikksekker fylt med forskjellige tomme bokser med energidrikker.\n" \
    "Du ser noen vinskap fylt med Red Bull og monster av forskjellige typer, og noe som ser ut som en fermenteringsbeholder som det står 'Monstervin' på.\n" \
    "På den ene veggen henger en stor oppslagstavle."
)
rom8_utforsk_tekst = (
    "Du står i det du bare kan anta er et gammeldags fyrrom basert på hva du har sett på film og TV. Midt i rommet står en gammel oljeovn.\n" \
    "I taket knirker en rusten vifte i vei, og flere rør går fra oljeovnen og opp til forskjellige punkter i taket. Oljekanner står rundt om kring i rommet.\n" \
    "På østveggen er det en stor ventil."
)

# Funksjon for beskrivelse av rom
def rombeskrivelse(romnavn, inngang, utforsk, besøkt):
    if not besøkt[romnavn]:
        print(inngang)       # Printes kun første gang
        besøkt[romnavn] = True
    print(utforsk)            # Printes hver gang spilleren går inn
    return besøkt

# Dict med oversikt over besøkte rom
besøkt = {
    "rom1": False,
    "rom2": False,
    "rom3": False,
    "rom4": False,
    "gang1": False,
    "rom5": False,
    "rom6": False,
    "rom7": False,
    "rom8": False
}

# Dict for interagerbare objekter
status = {
    "har_hammer": False,
    "har_brekkjern": False,
    "har_nøkkel": False,
    "rom3_skap": False,
    "tall1": False,
    "tall2": False,
    "tall3": False,
    "åpen_ventil": False,
    "falsk_nøkkel": False
}

# Funksjon som lister opp tallene spilleren har funnet
def tallkode_funnet(status):
    funnede_tall = []
    if status["tall1"]:
        funnede_tall.append("4")
    if status["tall2"]:
        funnede_tall.append("7")
    if status["tall3"]:
        funnede_tall.append("2")

    if funnede_tall:
        print("Så langt har du funnet tallene: " + ", ".join(funnede_tall))
    else:
        print("Du har ikke funnet noen tall enda!")


# Dict for gyldige valg i hvert rom
gyldige_valg_i_rom = {
    "rom1": ["vindu", "øst", "utforsk", "hjelp", "tallkode", "lagre"],
    "rom2": ["nord", "skap", "arbeidsbenk", "øst", "utforsk", "hjelp", "tallkode", "lagre"],
    "rom3": ["sør", "vest", "nord", "bokser", "malingsspann", "utforsk", "hjelp", "tallkode", "lagre"],
    "rom4": ["øst", "vest", "trapp", "skrivebord", "ventil", "utforsk", "hjelp", "tallkode", "lagre"],
    "gang1": ["sør", "nordøst", "nordvest", "sørøst", "sørvest", "utforsk", "hjelp", "tallkode", "lagre"],
    "rom5": ["sør", "esker", "kasser", "hyller", "reoler", "skap", "utforsk", "hjelp", "tallkode", "lagre"],
    "rom6": ["sør", "vaskemaskiner", "vaskemaskin", "hyller", "rør", "hjul", "utforsk", "hjelp", "tallkode", "lagre"],
    "rom7": ["nord", "vinskap", "plastsekker", "sekker", "oppslagstavle", "fermenteringsbeholder", "utforsk", "hjelp", "tallkode", "lagre"],
    "rom8": ["nord", "øst", "ovn", "oljeovn", "vifte", "rør", "ventil", "oljekanner", "utforsk", "hjelp", "tallkode", "lagre"]
}

# Funksjon som nullstiller besøkte rom
def nullstill_rom(romnavn, besøkt):
    besøkt[romnavn] = False

# Funksjon for å håndtere hjelp, utforsk, tallkode og lagre
def hjelp_og_utforsk(valg, hjelp_tekst, utforsk_tekst, status):
    if valg == "hjelp":
        print(hjelp_tekst)
    elif valg == "utforsk":
        print(utforsk_tekst)
    elif valg == "tallkode":
        tallkode_funnet(status)
    elif valg == "lagre":
        lagre_spill(besøkt, status, rom)

# Funksjon for når spilleren taper spillet
def tap_restart(tapmelding):
    print(tapmelding)
    while True:
        valg_restart = input(omstart).strip().lower()
        if valg_restart == "ja":
            return True, "rom1"
        elif valg_restart == "nei":
            quit()
        else:
            print(ugyldig)