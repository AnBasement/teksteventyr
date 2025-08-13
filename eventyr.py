###############################################################################
# eventyr.py
#
# Forfatter: AnBasement
# Versjon: 1.0.2
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

# Definerer variabler som blir brukt flere ganger
ugyldig = "Ugyldig svar, prøv igjen. "
omstart = "Vil du spille igjen? (ja/nei) "
tap = "Kjellerbeistet tok deg, og omverdenen hører aldri fra deg igjen."
spiller_prompt = "Hva vil du gjøre? "
hjelp = "Spillet liker bare ett-ords kommandoer – hold det enkelt!\nFor å bevege deg fra rom til rom kan du bruke himmelretningene.\nOm du har glemt hvor du er, kan du skrive 'utforsk' for en påminnelse."

# Variabel for rommet man befinner seg i. Begynner på "rom1" og endres avhengig av brukers valg.
rom = "rom1"

# Definerer variabelen "restart" som False
restart = False

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
    "Du trykker på en lysbryter ved siden av deg, og til din store overraskelse blir rommet godt opplyst av et par vegglamper.\n"
)
rom4_inngang_tekst = (
    "Idet du går gjennom den tomme dørkarmen i vest, kjenner du frisk luft treffe deg i ansiktet."
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
    "Der er en dør til sør, og en åpning mot vest."
)
rom4_utforsk_tekst = (
    "I midten av rommet står en trapp opp til etasjen over. Du ser en dør i enden av trappen.\n" \
    "Under trappen står et gammelt skrivebord med en stol.\n"
    "Der er en åpning på østveggen."
)

# Funksjon for beskrivelse av rom
def rombeskrivelse(romnavn, inngang, utforsk, besøkt):
    if not besøkt[romnavn]:
        print(inngang)
        print(utforsk)
        besøkt[romnavn] = True
    return besøkt

# Dict med oversikt over besøkte rom
besøkt = {
    "rom1": False,
    "rom2": False,
    "rom3": False,
    "rom4": False
}

# Dict for interagerbare objekter
status = {
    "har_hammer": False,
    "har_brekkjern": False,
    "har_nøkkel": False
}

# Dict for gyldige valg i hvert rom
gyldige_valg_i_rom = {
    "rom1": ["vindu", "øst", "utforsk", "hjelp"],
    "rom2": ["nord", "skap", "arbeidsbenk", "øst", "utforsk", "hjelp"],
    "rom3": ["sør", "vest", "bokser", "malingsspann", "utforsk", "hjelp"],
    "rom4": ["øst", "trapp", "skrivebord", "utforsk", "hjelp"]
}

# Funksjon som nullstiller besøkte rom
def nullstill_rom(romnavn, besøkt):
    besøkt[romnavn] = False

# Funksjon for å håndtere hjelp og utforsk
def hjelp_og_utforsk(valg, hjelp_tekst, utforsk_tekst):
    if valg == "hjelp":
        print(hjelp_tekst)
    elif valg == "utforsk":
        print(utforsk_tekst)

# Funksjon for når spilleren taper spillet
def tap_restart(tapmelding):
    print(tapmelding)
    while True:
        valg_restart = input(omstart).strip().lower()
        if valg_restart == "ja":
            return True
        elif valg_restart == "nei":
            quit()
        else:
            print(ugyldig)

# Funksjon for rom1
def rom_1(rom, restart, besøkt):
    while True: # Separat løkke for rom1
        besøkt = rombeskrivelse("rom1", rom1_inngang_tekst, rom1_utforsk_tekst, besøkt)

        valg = sjekk_gyldig_valg(spiller_prompt, gyldige_valg_i_rom["rom1"], ugyldig)

        if valg in ["hjelp", "utforsk"]:
            hjelp_og_utforsk(valg, hjelp, rom1_utforsk_tekst)
            continue

        if valg == "øst":
            rom = "rom2"
            break  # går videre til rom2
        elif valg == "vindu":
            restart = tap_restart("Du klatrer stigen opp mot vinduet. Idet du når toppen, knekker den sammen under deg. Du faller på nakken og alt går umiddelbart i svart.")
            break  # bryt rom1-løkka for å håndtere restart eller quit
        else:
            print(ugyldig)
    return rom, restart, besøkt

# Funksjon for rom2
def rom_2(rom, restart, status, besøkt):
    while True:  # separat løkke for rom2
        besøkt = rombeskrivelse("rom2", rom2_inngang_tekst, rom2_utforsk_tekst, besøkt)

        valg = sjekk_gyldig_valg(spiller_prompt, gyldige_valg_i_rom["rom2"], ugyldig)

        if valg in ["hjelp", "utforsk"]:
            hjelp_og_utforsk(valg, hjelp, rom2_utforsk_tekst)
            continue
        
        if valg == "nord":
            rom = "rom3"
            nullstill_rom("rom2", besøkt)
            break  # gå videre til rom3
        elif valg == "skap":
            print("Du åpner skapdørene, og støkker idet et rustent strykebrett faller over deg.\nEtter at nervene roer seg kikker du rundt i skapet, men ser ingenting av interesse.")
        elif valg == "arbeidsbenk":
            rom2_arbeidsbenk(status)
        elif valg == "øst":
            restart = rom2_ost(restart)
            if restart:
                break  # bryt rom2-løkka for å håndtere restart eller quit
        else:
            print(ugyldig)
    return rom, restart, status, besøkt

# Funksjon for arbeidsbenken i rom2
def rom2_arbeidsbenk(status):
    if not status["har_hammer"]:
        while True:
            svar = input("Arbeidsbenken består av relativt råttent treverk. Det ligger en hammer på den ene siden. Hva gjør du? ").lower().strip()
            if svar == "hjelp":
                print(hjelp)
            elif svar == "hammer":
                print("Idet du plukker opp hammeren, smuldrer treskaftet opp...")
                status["har_hammer"] = True
                break
            else:
                print(ugyldig)
    else:
        print("Arbeidsbenken består av relativt råttent treverk.")

# Funksjon for å velge øst i rom 2
def rom2_ost(restart):
    while True:
        svar = input("Etterhvert som du nærmer deg døren på østveggen hører du bevegelse og noe som høres ut som grynting på andre siden av døren. Vil du åpne den? (ja/nei) ").lower().strip()
        if svar == "ja":
            restart = tap_restart(tap)
            return restart
        elif svar == "nei":
            break  # tilbake til rom2 uten å gjøre noe
        else:
            print(ugyldig)

# Funksjon for rom 3
def rom_3(rom, restart, status, besøkt):
    while True: # Løkke for rom 3
        besøkt = rombeskrivelse("rom3", rom3_inngang_tekst, rom3_utforsk_tekst, besøkt)

        valg = sjekk_gyldig_valg(spiller_prompt, gyldige_valg_i_rom["rom3"], ugyldig)

        if valg in ["hjelp", "utforsk"]:
            hjelp_og_utforsk(valg, hjelp, rom3_utforsk_tekst)
            continue

        if valg == "sør":
            rom = "rom2"
            nullstill_rom("rom3", besøkt) # nullstill for neste gang
            break  # gå tilbake til rom2
        elif valg == "malingsspann":
            rom3_malingsspann(status)
        elif valg == "bokser":
            print("En haug med det som ser ut til å en gang ha vært pappesker, men er nå en haug med forråtnende papp.")
        elif valg == "vest":
            rom = "rom4"
            nullstill_rom("rom3", besøkt) # nullstill for neste gang
            break  # gå videre til rom4
    return rom, restart, status, besøkt

# Funksjon for malingsspann i rom 3
def rom3_malingsspann(status):
    while True:
        if not status["har_nøkkel"]:  # Sjekker om spilleren har nøkkelen
            if not status["har_brekkjern"]:  # Sjekker om spilleren har brekkjernet
                print(
                    "Du plukker opp noen av malingsspannene, og hører noe løst inni en av dem.\n"
                    "Du forsøker å åpne den, men inntørket maling og rust har gjort det nesten umulig."
                )
            else: # Spilleren har brekkjernet
                print(
                    "Du bruker det lille brekkjernet du fant til å åpne malingsspannet som hadde noe inni seg.\n"
                    "Inni finner du en gammeldags nøkkel!"
                )
                status["har_nøkkel"] = True # Spilleren får nøkkelen
                break
        else:
            print("En haug med gamle malingsspann.") # Spilleren har allerede nøkkelen
        break
    
    return status # Returnerer oppdatert status

# Funksjon for rom4
def rom_4(rom, restart, status, besøkt):
    while True:  # Løkke for rom 4
        besøkt = rombeskrivelse("rom4", rom4_inngang_tekst, rom4_utforsk_tekst, besøkt)

        valg = sjekk_gyldig_valg(spiller_prompt, gyldige_valg_i_rom["rom4"], ugyldig)

        if valg in ["hjelp", "utforsk"]:
            hjelp_og_utforsk(valg, hjelp, rom4_utforsk_tekst)
            continue

        if valg == "trapp":
            restart, rom = rom4_trapp(status)
            if restart:  # Spill fullført, bryt løkka
                break
        elif valg == "skrivebord":
            rom4_skrivebord(status)
        elif valg == "øst":
            rom = "rom3"
            nullstill_rom("rom4", besøkt)  # nullstill for neste gang
            break  # gå videre til rom3
    return rom, restart, status, besøkt

# Funksjon for trapp i rom 4
def rom4_trapp(status):
    if status["har_nøkkel"]:  # Sjekker om spilleren har nøkkelen
        print("Du klatrer opp til døren i toppen av trappen, og setter den gamle nøkkelen i nøkkelhullet.\n"
              "Du hører et tydelig *klikk* når du vrir den. Med noe makt klarer du å vri om håndtaket, åpne døren, og rømme ut av kjelleren.\n"
              "Gratulerer! Du har unngått Kjellerbeistet og rømt fra kjelleren!")
        while True:
            valg_restart = input(omstart).strip().lower()
            if valg_restart == "ja":
                return True, "rom1"  # restart = True, rom = rom1
            elif valg_restart == "nei":
                quit()
            else:
                print(ugyldig)
    else:
        print("Du klatrer opp den morkne trappa og vrir om håndtaket på døren.\n"
              "Samme hvor hardt du prøver, lar den ikke bevege på seg. Du merker et gammeldags nøkkelhull under håndtaket.")
        return False, "rom4"

# Funksjon for skrivebord i rom 4
def rom4_skrivebord(status):
    if not status["har_brekkjern"]:
        print("Det som uten tvil var et vakkert møbel en gang er nå slitt og råtnende. Noen av skuffene mangler, men du finner et brekkjern i en av de som fremdeles består.")
        status["har_brekkjern"] = True
    else:
        print("Et gammelt og godt brukt skrivebord med noen tomme skuffer.")

    return status

print("""Velkommen til det tekstbaserte eventyret 'Beistet i kjelleren'!
Du må forsøke å navigere deg til trappen og ut av kjelleren uten å støte på beistet.
Om du trenger hjelp kan du skrive 'hjelp' for en liste over godkjente kommandoer.""")

# Krever at spiller skriver "start" for å begynne
while True:
    start = input('Skriv "start" for å begynne. ').strip().lower()
    if start == "start":
        break
    print(ugyldig)
    
# Begynner spillet
while True:
    if restart:
        rom = "rom1"
        for rom_navn in besøkt:
            besøkt[rom_navn] = False
    
        # Nullstill status
        for key in status:
            status[key] = False
    
    restart = False

    # Hovedløkke for å navigere gjennom rommene
    if rom == "rom1":
        rom, restart, besøkt = rom_1(rom, restart, besøkt)
    elif rom == "rom2":
        rom, restart, status, besøkt = rom_2(rom, restart, status, besøkt)
    elif rom == "rom3":
        rom, restart, status, besøkt = rom_3(rom, restart, status, besøkt)
    elif rom == "rom4":
        rom, restart, status, besøkt = rom_4(rom, restart, status, besøkt)