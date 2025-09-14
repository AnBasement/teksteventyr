# Inneholder alt av hjelpefunksjoner.

import os
import kartdata as kart
import json
import random

# =========================
# Globale variabler og stier
# =========================

# Filsti for lagring av spill
lagret_spill = os.path.join(os.path.dirname(__file__), "savegame.json")

# Nåværende rom
rom = "rom1"

# Restart-variabel
restart = False

# Feilmeldinger og prompts
ugyldig = "Ugyldig svar, prøv igjen. "
omstart = "Vil du spille igjen? (ja/nei) "
tap = "Kjellerbeistet tok deg, og omverdenen hører aldri fra deg igjen."
spiller_prompt = "Hva vil du gjøre? "
hjelp = (
    "Spillet godkjenner bare enkle kommandoer som må starte med 'gå', 'se' eller 'ta'. Du kan også bruke noe i inventaret ditt ved å skrive 'bruk gjenstand objekt'\n"
    "For å bevege deg fra rom til rom kan du bruke himmelretningene (nord, sør, sørvest etc.).\n"
    "Om du har glemt hvor du er, kan du skrive 'utforsk' for å se rommet igjen, eller 'tallkode' for en påminnelse om koden! "
    "Om du har funnet det, kan du også skrive 'kart' for en oversikt over kjelleren. Du kan også skrive 'lagre' for å lagre fremgangen din."
)
ingen_vei = "Det er ingen vei i den retningen."
not_objekt = "Du har ikke det i inventaret."

# =========================
# Romtekster
# =========================

# Tekst som vises når man går inn i rommet første gang
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
rom9_inngang_tekst = (
    "Du dytter på det løse panelet, som sklir opp og avslører et skjult rom på den andre siden."
)
rom10_inngang_tekst = (
    "Det øyeblikket du dytter opp døren kommer en støvsky ut og treffer deg i ansiktet. Etter et hosteanfall ser du deg rundt i det nye rommet."
)
rom11_inngang_tekst = (
    "Du åpner døren og blir møtt av et bekmørkt rom. Lyset fra fyrrommet lyser ikke opp mer enn en meter inn."
)
rom12_inngang_tekst = (
    "Du åpner døren til et trangt, kaldt rom. En svak lukt av mugg og gammel mat slår mot deg."
)
rom13_inngang_tekst = (
    "Den smale åpningen leder inn i et fuktig, lavt kammer. De eneste lydene du hører er den konstante dryppingen fra det fuktige taket."
)
kjeller2_1_inngang_tekst = (
    "Den bratte trappen ender i en mørk, kald del av kjelleren. Veggene er grov stein, og vann drypper fra taket."
)
kjeller2_2_inngang_tekst = (
    "Du går inn i et rom som ser ut som en blanding av laboratorium og torturkammer."
)

# Tekst som vises ved "utforsk"-kommando
rom1_utforsk_tekst = (
    "Du befinner deg i et mørkt rom med et lite, skittent vindu like under taket til vest med en stige under. Til øst er det en dør."
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
    "I midten av rommet står en trapp opp til etasjen over. Du ser en dør i enden av trappen.\n"
    "Under trappen står et gammelt skrivebord med en stol. På den ene veggen ser du en stor ventil.\n"
    "Der er en åpning på østveggen."
)
gang1_utforsk_tekst = (
    "Du står i en lang gang. Foran deg ser du to dører, en til nordvest og en til nordøst.\n"
    "Gangen strekker seg fra vest til øst, og når du ser deg rundt ser du også dører til sørvest og sørøst.\n"
    "Gangen er opplyst av spottere, og fremstår ellers som helt bar."
)
rom5_utforsk_tekst = (
    "Du finner deg omringet av høye stabler av kasser og esker. To høye reoler står midt i rommet, og langs den bakre veggen står et enkelt skap. En sliten hylle står lent mot østveggen. En dør leder sør."
)
rom6_utforsk_tekst = (
    "Du står i noe som ligner på en vaskekjeller. Det står to vaskemaskiner stablet opp langs den ene veggen.\n"
    "Den bakre veggen og taket er fullt av rør, noen med små lekkasjer og andre så rustne at det er et under de ikke lekker. På ett av rørene er det et stort rødt hjul, og du legger merke til noe som ligner på en løs paneldør ved siden.\n"
    "Langs den siste veggen står en rekke hyller med forskjellige vaskemidler på. Dører leder sør og nord."
)
rom7_utforsk_tekst = (
    "Rommet minner om en vinkjeller for en tenåringsgutt. Langs veggene ligger store plastikksekker fylt med forskjellige tomme bokser med energidrikker.\n"
    "Du ser noen vinskap fylt med Red Bull og monster av forskjellige typer, og noe som ser ut som en fermenteringsbeholder som det står 'Monstervin' på.\n"
    "På den ene veggen henger en stor oppslagstavle. En dør leder nord."
)
rom8_utforsk_tekst = (
    "Du står i det du bare kan anta er et gammeldags fyrrom basert på hva du har sett på film og TV. Midt i rommet står en gammel oljeovn.\n"
    "I taket knirker en rusten vifte i vei, og flere rør går fra oljeovnen og opp til forskjellige punkter i taket. Oljekanner står rundt om kring i rommet.\n"
    "På østveggen er det en stor ventil. Dører leder nord og sør."
)
rom9_utforsk_tekst = (
    "Du står i et rom som ser ut til å ha vært hogget ut av steinen rundt kjelleren.\n"
    "Luften er tung og fuktig, og de grove veggene er dekket av noe som ser ut som glødende sopp. I et hjørne står en gammel bøtte med noe mørkt og flytende oppi.\n"
    "Noen av soppene ser nesten ut til å ha ansikter på seg, men det kan vel ikke stemme? En dør leder sør."
)
rom10_utforsk_tekst = (
    "Rommet kan bare beskrives som et slags gammelt arkivrom. Stabler av gamle aviser, magasiner og blader og hyller med bøker over hele rommet.\n"
    "Midt i rommet står en pult med en gammel pizzaeske, en haug med avisutklipp og en slags manual på.\n"
    "Du får inntrykk av at rommet ikke har hatt besøkende på lang tid. Dører leder vest og øst."
)
rom11_utforsk_tekst = (
    "Det mørke rommet er relativt tomt. Et tykt lag støv ligger på gulvet, avbrutt kun av fotspor som leder fem og tilbake mellom døren og en luke i gulvet.\n"
    "Luken, som ser relativt solid ut, har et messingskilt på seg. En dør leder nord."
)
rom12_utforsk_tekst = (
    "Rundt i rommet står en rekke hyller og kasser. Noen av kassene er ødelagte, og på gulvet ligger en pose med noe hvitt i. "
    "På den ene veggen henger en jernkrok, og i et hjørne står en umerket krukke. " \
    "Der er dører som leder vest og sør."
)
rom13_utforsk_tekst = (
    "Kammeret har steinvegger som drypper vann, og gulvet er fuktig. "
    "Rommet ser relativt tomt ut, sett bort fra en sokkel midt i rommet med et gammeldags skrin på. Det ser ut til at noen har risset noe inn i veggene. " \
    "Der en utgang som leder nord."
)
kjeller2_1_utforsk_tekst = (
    "Du står i bunnen av stigen. En stige går langs den ene veggen, men ser ikke ut til å lede noe sted. "
    "Veggene er grove og ser nesten ut til å være hogget ut manuelt, og du hører konstant sildring og drypping. "
    "Til øst ser du en døråpning."
)
kjeller2_2_utforsk_tekst = (
    "Rommet har et trykkende preg. Nedstøvete bokhyller står langs veggene, og både gulvet og bordene er dekket med kolber i varierende stand. "
    "På et bord står et gammelt treskrin med hengelås, tydelig tilsynelatende verdifullt. Langs den ene veggen er et verktøyskap. "
    "En dør leder vest."
)

# Dict som kobler rom til utforsk-tekst
utforsk_tekster = {
    "rom1": rom1_utforsk_tekst,
    "rom2": rom2_utforsk_tekst,
    "rom3": rom3_utforsk_tekst,
    "rom4": rom4_utforsk_tekst,
    "gang1": gang1_utforsk_tekst,
    "rom5": rom5_utforsk_tekst,
    "rom6": rom6_utforsk_tekst,
    "rom7": rom7_utforsk_tekst,
    "rom8": rom8_utforsk_tekst,
    "rom9": rom9_utforsk_tekst,
    "rom10": rom10_utforsk_tekst,
    "rom11": rom11_utforsk_tekst,
    "rom12": rom12_utforsk_tekst,
    "rom13": rom13_utforsk_tekst,
    "kjeller2_1": kjeller2_1_utforsk_tekst,
    "kjeller2_2": kjeller2_2_utforsk_tekst,
}

# =========================
# Spill-tilstand
# =========================

# Oversikt over besøkte rom
besøkt = {
    "rom1": False,
    "rom2": False,
    "rom3": False,
    "rom4": False,
    "gang1": False,
    "rom5": False,
    "rom6": False,
    "rom7": False,
    "rom8": False,
    "rom9": False,
    "rom10": False,
    "rom11": False,
    "rom12": False,
    "rom13": False,
    "kjeller2_1": False,
    "kjeller2_2": False,
}

# Interagerbare objekter
status = {
    "har_hammer": False,
    "rom2_skap": False,
    "tall1": False,
    "tall2": False,
    "tall3": False,
    "åpen_ventil": False,
    "bøtte": False,
    "åpen_hylle": False,
    "hengelås": False,
    "luke_kode": False,
    "åpen_luke": False,
    "krukke": False,
    "rom13_skrin": False,
    "skrin13": 0,
    "skrin2_2": 0,
    "ventil": 0,
    "malingsspann": 0,
    "kolber": False,
    "helse": 3,
    "poeng": 0
}

# Inventar
inventar = {
    "brekkjern": False,
    "har_nøkkel": False,
    "falsk_nøkkel": False,
    "glødende_sopp": False,
    "kart": False,
    "saltpose": False,
    "jernkrok": False,
    "luke_nøkkel1": False,
    "luke_nøkkel2": False,
}

# Vekter for sjansemekanikk
sjanser = {
    "rom13_vekter": [(50, 50), (75, 25), (100, 0)],
    "malingsspann": [(50, 50), (75, 25), (100, 0)],
    "ventil": [(50, 50), (75, 25), (100, 0)],
    "kjeller2_2_vekter": [(50, 50), (75, 25), (100, 0)]
}

# Gyldige valg i hvert rom
gyldige_valg_i_rom = {
    "rom1": ["vindu", "øst", "utforsk", "hjelp", "tallkode", "lagre", "kart", "helse"],
    "rom2": ["nord", "skap", "arbeidsbenk", "hammer", "øst", "utforsk", "hjelp", "tallkode", "lagre", "kart", "helse"],
    "rom3": ["sør", "vest", "nord", "bokser", "malingsspann", "utforsk", "hjelp", "tallkode", "lagre", "kart", "helse"],
    "rom4": ["øst", "vest", "trapp", "dør", "skrivebord", "hengelås", "ventil", "utforsk", "hjelp", "tallkode", "lagre", "kart", "helse"],
    "gang1": ["sør", "nordøst", "nordvest", "sørøst", "sørvest", "utforsk", "hjelp", "tallkode", "lagre", "kart", "helse"],
    "rom5": ["sør", "øst", "esker", "kasser", "hyller", "hylle", "reoler", "skap", "utforsk", "hjelp", "tallkode", "lagre", "kart", "helse"],
    "rom6": ["sør", "nord", "vaskemaskiner", "vaskemaskin", "hyller", "rør", "hjul", "utforsk", "hjelp", "tallkode", "lagre", "kart", "helse"],
    "rom7": ["nord", "vinskap", "plastsekker", "sekker", "oppslagstavle", "fermenteringsbeholder", "utforsk", "hjelp", "tallkode", "lagre", "kart", "helse"],
    "rom8": ["nord", "øst", "ovn", "oljeovn", "vifte", "rør", "ventil", "oljekanner", "utforsk", "hjelp", "tallkode", "lagre", "kart", "helse"],
    "rom9": ["sør", "sopp", "glødende sopp", "bøtte", "utforsk", "hjelp", "tallkode", "lagre", "kart", "helse"],
    "rom10": ["vest", "aviser", "magasiner", "pult", "pizzaeske", "manual", "avisutklipp", "utforsk", "hjelp", "tallkode", "lagre", "kart", "helse"],
    "rom11": ["nord", "fotspor", "luke", "skilt", "messingskilt", "nøkkel", "kode", "utforsk", "hjelp", "tallkode", "lagre", "kart", "helse"],
    "rom12": ["øst", "sør", "hylle", "hyller", "kasse", "kasser", "filler", "stoffrester", "pose", "jernkrok", "krok", "krukke", "nøkkel", "gugge", "utforsk", "hjelp", "tallkode", "lagre", "kart", "helse"],
    "rom13": ["nord", "skrin", "sokkel", "vegg", "vegger", "brekkjern", "utforsk", "hjelp", "tallkode", "lagre", "kart", "helse"],
    "kjeller2_1": ["luke", "øst", "stige", "jernstige", "vegg", "vegger", "utforsk", "hjelp", "tallkode", "lagre", "kart", "helse"],
    "kjeller2_2": ["vest", "bokhylle", "bokhyller", "kolbe", "kolber", "skrin", "brekkjern", "utforsk", "hjelp", "tallkode", "lagre", "kart", "helse"],
}

# =========================
# Funksjoner
# =========================

# Lagre spillstatus
def lagre_spill(besøkt, status, rom):
    data = {
        "besøkt": besøkt,
        "status": status,
        "inventar": inventar,
        "rom": rom
    }
    with open(lagret_spill, "w", encoding="utf-8") as fil:
        json.dump(data, fil, ensure_ascii=False, indent=4)
    print("Spillet ditt er lagret!")

# Laste inn spillstatus
def last_inn_spill():
    global besøkt, status, rom
    if not os.path.exists(lagret_spill):
        print("Finner ikke et lagret spill, starter et nytt!")
        return besøkt, status, rom

    with open(lagret_spill, "r", encoding="utf-8") as fil:
        data = json.load(fil)
        besøkt = data.get("besøkt", besøkt)
        status = data.get("status", status)
        rom = data.get("rom", rom)
        inventar.update(data.get("inventar", inventar))  # Oppdaterer eksisterende inventar

    print("Velkommen tilbake!")
    return besøkt, status, rom

# Funksjon for å sjekke gyldige valg
def sjekk_gyldig_valg(prompt, gyldige_valg, ugyldig):
    while True:
        valg = input(prompt).strip().lower()
        if valg in gyldige_valg:
            return valg
        print(ugyldig)

# Funksjon for beskrivelse av rom
def rombeskrivelse(romnavn, inngang, utforsk, besøkt):
    if not besøkt[romnavn]:
        print(inngang) 
        besøkt[romnavn] = True
    print(utforsk)
    return besøkt

# Funksjon som sjekker om spiller har en gjenstand
def har_gjenstand(obj):
    return obj in inventar and inventar[obj]

# Feilmelding ved bruk av feil gjenstand
def bruk_feilmelding(obj):
    return f"Du prøver å bruke {obj}, men det fungerer ikke her."

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

# Funksjon som endrer antall helsepoeng
def endre_helse(endring: int):
    global status, rom
    status["helse"] += endring

    if status["helse"] <= 0:
        # Spilleren har mistet all helse
        tapmelding = "Du har mistet alle helsepoengene dine!"
        restart, rom = tap_restart(tapmelding)
        if restart:
            # Nullstill helse og besøkt/inventar
            status["helse"] = 3
            for key in besøkt:
                besøkt[key] = False
            for key in inventar:
                inventar[key] = False

# Funksjon for sjansemekanikk
def sjansemekanikk(hendelse, status):
    status[hendelse] = status.get(hendelse, 0) + 1
    forsøk = status(hendelse)

    vekter = sjanser(hendelse)
    w = vekter[min(forsøk - 1, len(vekter) - 1)]

    return random.choices(["seier", "tap"], weights = w) [0]

# Funksjon som nullstiller besøkte rom
def nullstill_rom(romnavn, besøkt):
    besøkt[romnavn] = False

# Funksjon for å håndtere hjelp, utforsk, tallkode, lagre, kart og helse
def hjelp_og_utforsk(valg, hjelp_tekst, utforsk_tekst, status):
    if valg == "hjelp":
        print(hjelp_tekst)
    elif valg == "utforsk":
        print(utforsk_tekst)
    elif valg == "tallkode":
        tallkode_funnet(status)
    elif valg == "lagre":
        lagre_spill(besøkt, status, rom)
    elif valg == "kart":
        if not inventar["kart"]:
            print(ugyldig)
        else:
            kart.vis_kart()
    elif valg == "helse":
        print(status["helse"])

# Parser for to- og tre-ords kommandoer
def parse_kommando():
    while True:
        kommando_input = input("> ").strip().lower()
        kommando = kommando_input.split()

        # Én-ords kommando
        if len(kommando) == 1:
            ord1 = kommando[0]
            if ord1 in ["hjelp", "utforsk", "tallkode", "lagre", "kart"]:
                hjelp_og_utforsk(ord1, hjelp, utforsk_tekster[rom], status)
            else:
                print(ugyldig)
            continue

        # To-ords kommando
        elif len(kommando) == 2:
            verb, obj = kommando

            if verb not in ["gå", "se", "ta", "bruk"]:
                print(f"Kjenner ikke kommandoen {verb}.")
                continue

            if verb == "bruk" and obj in inventar and inventar[obj]:
                print(f"Hva vil du bruke {obj} på?")
                mål = input("> ").strip().lower()
                if mål not in gyldige_valg_i_rom[rom]:
                    print(f"Jeg ser ingen {mål} her.")
                    continue
                return verb, (obj, mål)

            if obj not in gyldige_valg_i_rom[rom]:
                print(f"Jeg forstår ikke hva du mener med {obj}.")
                continue
            return verb, obj

        # Tre-ords kommando
        elif len(kommando) == 3:
            verb, obj1, obj2 = kommando
            if verb == "bruk":
                if obj1 not in inventar or not inventar[obj1]:
                    print(f"Du har ikke {obj1} i inventaret.")
                    continue
                if obj2 not in gyldige_valg_i_rom[rom]:
                    print(f"Jeg ser ingen {obj2} her.")
                    continue
                return verb, (obj1, obj2)
            else:
                print(ugyldig)
                continue

        else:
            print(ugyldig)

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
