# Fil som inneholder alle rommene.

import engine

# Funksjon for rom1
def rom1(rom, restart, besøkt):
    besøkt = rombeskrivelse("rom1", rom1_inngang_tekst, rom1_utforsk_tekst, besøkt)
    while True: # Separat løkke for rom1

        valg = sjekk_gyldig_valg(spiller_prompt, gyldige_valg_i_rom["rom1"], ugyldig)

        if valg in ["hjelp", "utforsk", "tallkode", "lagre"]:
            hjelp_og_utforsk(valg, hjelp, rom1_utforsk_tekst, status)
            continue

        if valg == "øst":
            rom = "rom2"
            break  # går videre til rom2
        elif valg == "vindu":
            restart, rom = tap_restart("Du klatrer stigen opp mot vinduet. Idet du når toppen, knekker den sammen under deg. Du faller på nakken og alt går umiddelbart i svart.")
            break  # bryt rom1-løkka for å håndtere restart eller quit
        else:
            print(ugyldig)
    return rom, restart, besøkt

# Funksjon for rom2
def rom2(rom, restart, status, besøkt):
    besøkt = rombeskrivelse("rom2", rom2_inngang_tekst, rom2_utforsk_tekst, besøkt)
    while True:  # separat løkke for rom2

        valg = sjekk_gyldig_valg(spiller_prompt, gyldige_valg_i_rom["rom2"], ugyldig)

        if valg in ["hjelp", "utforsk", "tallkode", "lagre"]:
            hjelp_og_utforsk(valg, hjelp, rom2_utforsk_tekst, status)
            continue
        
        if valg == "nord":
            rom = "rom3"
            break  # gå videre til rom3
        elif valg == "skap":
            if not status["rom3_skap"]:
                print("Du åpner skapdørene, og støkker idet et rustent strykebrett faller over deg.\nEtter at nervene roer seg kikker du rundt i skapet, men ser ingenting av interesse.")
            else:
                print("Vaskebrettet ligger på gulvet, resten av skapet er uinteressant.")
        elif valg == "arbeidsbenk":
            rom2_arbeidsbenk(status)
        elif valg == "øst":
            restart, rom = rom2_ost(restart)
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
            restart, rom = tap_restart(tap)
            return restart, rom
        elif svar == "nei":
            return False, "rom2"
        else:
            print(ugyldig)

# Funksjon for rom 3
def rom3(rom, restart, status, besøkt):
    besøkt = rombeskrivelse("rom3", rom3_inngang_tekst, rom3_utforsk_tekst, besøkt)
    while True: # Løkke for rom 3

        valg = sjekk_gyldig_valg(spiller_prompt, gyldige_valg_i_rom["rom3"], ugyldig)

        if valg in ["hjelp", "utforsk", "tallkode", "lagre"]:
            hjelp_og_utforsk(valg, hjelp, rom3_utforsk_tekst, status)
            continue

        if valg == "sør":
            rom = "rom2"
            break
        elif valg == "malingsspann":
            rom3_malingsspann(status)
        elif valg == "bokser":
            print("En haug med det som ser ut til å en gang ha vært pappesker, alle merket med tallet '4', men er nå en haug med forråtnende papp.")
            status["tall1"] = True
        elif valg == "vest":
            rom = "rom4"
            break
        elif valg == "nord":
            rom = "gang1"
            break
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
def rom4(rom, restart, status, besøkt):
    if not besøkt["rom4"]:
        print(rom4_inngang_tekst)
        besøkt["rom4"] = True

    if status["åpen_ventil"]:
        print("I midten av rommet står en trapp opp til etasjen over. Du ser en dør i enden av trappen.\n" \
    "Under trappen står et gammelt skrivebord med en stol. På vestveggen er det et åpent hull.\n"
    "Der er en åpning på østveggen."
    )
    else:
        print(rom4_utforsk_tekst)
        
    while True:

        valg = sjekk_gyldig_valg(spiller_prompt, gyldige_valg_i_rom["rom4"], ugyldig)

        if valg in ["hjelp", "utforsk", "tallkode", "lagre"]:
            hjelp_og_utforsk(valg, hjelp, rom4_utforsk_tekst, status)
            continue

        if valg == "trapp":
            restart, rom = rom4_trapp(status)
            if restart:  # Spill fullført, bryt løkka
                break
        elif valg == "skrivebord":
            rom4_skrivebord(status)
        elif valg == "ventil":
            if not status["åpen_ventil"]:
                print("En stor ventil er plassert midt på vestveggen. Det kommer varm luft fra den andre siden.")
            else:
                print(ugyldig)
        elif valg == "vest":
            if status["åpen_ventil"]:
                rom = "rom8"
                break
            else:
                print(ugyldig)
        elif valg == "øst":
            rom = "rom3"
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
    elif status["falsk_nøkkel"]:
        restart, rom = tap_restart("Med litt makt klarer du å presse nøkkelen du fant inn i nøkkelhullet.\n"
        "Du rister litt i nøkkelen i et forsøk på å vri den rundt, men nøkkelen knekker. Plutselig uler en alarm gjennom kjelleren.\n"
        "Du hører en rytmisk dundring som blir høyere, og et gutturalt rop. Du rekker knapt å snu deg for å se inn i et fettete, kvisete ansikt før alt går i sort.")
        return restart, rom
    else:
        print("Du klatrer opp den morkne trappa og vrir om håndtaket på døren.\n"
              "Samme hvor hardt du prøver, lar den ikke bevege på seg. Du merker et gammeldags nøkkelhull under håndtaket.")
        return False, "rom4"

# Funksjon for skrivebord i rom 4
def rom4_skrivebord(status):
    if status.get("har_brekkjern"):
        print("Et gammelt og godt brukt skrivebord med noen tomme skuffer.")
        return status
    while True:
        kode_input = input(
            "Det som uten tvil var et vakkert møbel en gang er nå slitt og råtnende. "
            "Alle skuffene mangler utenom én, men den er låst med en 3-sifret hengelås. "
            "Tast inn koden eller skriv 'avbryt': "
        ).strip()
        if kode_input.lower() == "avbryt":
            print("Du avbryter forsøket på å åpne skuffen.")
            break
        try:
            skrivebord_kode = int(kode_input)
        except ValueError:
            print("Du må taste inn tall.")
            continue
        if skrivebord_kode == 472:
            print("Med riktig kode får du av hengelåsen. Oppi skuffen ligger et brekkjern, som du plukker opp.")
            status["har_brekkjern"] = True
            break
        else:
            print("Feil kode. Prøv igjen.")
    return status

# Funksjon for gang1
def gang1(rom, restart, status, besøkt):
    besøkt = rombeskrivelse("gang1", gang1_inngang_tekst, gang1_utforsk_tekst, besøkt)
    while True:  # Løkke for gang 1

        valg = sjekk_gyldig_valg(spiller_prompt, gyldige_valg_i_rom["gang1"], ugyldig)

        if valg in ["hjelp", "utforsk", "tallkode", "lagre"]:
            hjelp_og_utforsk(valg, hjelp, gang1_utforsk_tekst, status)
            continue

        if valg == "sør":
            rom = "rom3"
            break  # gå videre til rom3
        elif valg == "nordvest":
            rom = "rom6"
            break  # gå videre til rom6
        elif valg == "nordøst":
            rom = "rom5"
            break  # gå videre til rom5
    return rom, restart, status, besøkt

# Funksjon for rom5
def rom5(rom, restart, status, besøkt):
    besøkt = rombeskrivelse("rom5", rom5_inngang_tekst, rom5_utforsk_tekst, besøkt)
    while True:  # Løkke for rom5

        valg = sjekk_gyldig_valg(spiller_prompt, gyldige_valg_i_rom["rom5"], ugyldig)

        if valg in ["hjelp", "utforsk", "tallkode", "lagre"]:
            hjelp_og_utforsk(valg, hjelp, rom5_utforsk_tekst, status)
            continue

        if valg == "sør":
            rom = "gang1"
            break  # gå videre til gang
        elif valg == "esker":
            print("Du ser over stablene av esker som står spredd langs veggene, i varierende grad av forråtnelse.\n" \
            "Du åpner noen vilkårlige esker, og finner noen fylt med gamle tegneserier, andre med gamle spill, og underlig nok en tredje full av flasker fylt med en gul væske.")
        elif valg == "hyller":
            print("Du går frem og tilbake i rommet og saumfarer hyllene etter noe nyttig.\n" \
            "På noen av hyllene står det noen gamle lekefigurer, men du finner ingenting av nytte.")
        elif valg == "skap":
            print("Bakerst i rommet står det et skap som minner deg om skoledagene dine. Sett bort fra tallet '7' på forsiden er det ingenting uvanlig med det.\n" \
            "Du tar tak i håndtaket og røsker til, men skapet beveger seg ikke.")
            status["tall2"] = True
    return rom, restart, status, besøkt

# Funksjon for rom6
def rom6(rom, restart, status, besøkt):
    besøkt = rombeskrivelse("rom6", rom6_inngang_tekst, rom6_utforsk_tekst, besøkt)
    while True: # Løkke for rom6

        valg = sjekk_gyldig_valg(spiller_prompt, gyldige_valg_i_rom["rom6"], ugyldig)

        if valg in ["hjelp", "utforsk", "tallkode", "lagre"]:
            hjelp_og_utforsk(valg, hjelp, rom6_utforsk_tekst, status)
            continue

        if valg == "sør":
            rom = "gang1"
            break # Gå tidere til gang
        elif valg in ["vaskemaskiner", "vaskemaskin"]:
            print("Vaskemaskinene er i dårlig stand, og tydeligvis ikke brukt på en stund. Det ligger en haug med råtne klær i den ene, og ingen av dem reagerer når du trykker på knappene.")
        elif valg == "hyller":
            print("Du ser fort over hyllene etter noe som kan hjelpe deg, men ser stort sett bare forskjellige vaskemidler av merket '2MO'.")
            status["tall3"] = True
        elif valg in ["rør", "hjul"]:
            restart, rom = rom6_hjul(restart)
            if restart:
                break
    return rom, restart, status, besøkt

# Funksjon for å velge hjul eller rør i rom 6
def rom6_hjul(restart):
    while True:
        svar = input("Det største av rørene har et rødt hjul festet til seg. Du tar borti røret, og kan kjenne at det beveger seg vann gjennom det. Vil du vri på hjulet? (ja/nei) ").lower().strip()
        if svar == "ja":
            restart, rom = tap_restart("Med noe makt klarer du å vri om på hjulet. Det begynner umiddelbart å fosse vann ut av vaskemaskinene, og et gitter smeller ned foran døren.\n" \
            "Du prøver desperat å snu hjulet tilbake, men det sitter låst fast. Du forsøker å rive opp gitteret, men det rikker seg ikke.\n" \
            "Det tar bare noen sekunder før rommet er fylt med vann. Uten luft svelger du ned vann, og alt går i sort.")
            return restart, rom
        elif svar == "nei":
            return False, "rom6" 
        else:
            print(ugyldig)

# Funksjon for rom 7 - monsterkjelleren
def rom7(rom, restart, status, besøkt):
    besøkt = rombeskrivelse("rom7", rom7_inngang_tekst, rom7_utforsk_tekst, besøkt)
    while True:

        valg = sjekk_gyldig_valg(spiller_prompt, gyldige_valg_i_rom["rom7"], ugyldig)

        if valg in ["hjelp", "utforsk", "tallkode", "lagre"]:
            hjelp_og_utforsk(valg, hjelp, rom7_utforsk_tekst, status)
            continue

        if valg == "nord":
            rom = "gang1"
            break
        elif valg == "plastsekker":
            print("Fem stappfulle plastsekker er stablet opp langs den ene veggen. Du roter litt oppi noen av dem, men gir opp når hendene dine blir klissete.")
        elif valg == "vinskap":
            print("Det er ikke første gang du ser et vinskap, men det er første gang du ser et vinskap fult av forskjellige energidrikker. Noen av dem har støv på seg og ser gamle ut.")
        elif valg == "fermenteringsbeholder":
            print("I det ene hjørnet bobler det i vei i det du bare kan anta er et forsøk på å lage vin av energidrikk. Du tar et lite sniff og rynker på nesen, frister ikke særlig.")
        elif valg == "oppslagstavle":
            print("Det henger et par forskjellige lapper på oppslagstavlen som ser ut til å indikere datoer på tidligere og det nåværende fermenteringsprosjektet.\n" \
                  "På en gul lapp står det '!NB! Esker, skap, såpe!'")
    return rom, restart, status, besøkt
            
# Funksjon for rom 8 - Fyrrommet
def rom8(rom, restart, status, besøkt):
    if not besøkt["rom8"]:
        print(rom8_inngang_tekst)
    besøkt["rom8"] = True

    if status["åpen_ventil"]:
        print("Du står i det du bare kan anta er et gammeldags fyrrom basert på hva du har sett på film og TV. Midt i rommet står en gammel oljeovn.\n" \
    "I taket knirker en rusten vifte i vei, og flere rør går fra oljeovnen og opp til forskjellige punkter i taket. Oljekanner står rundt om kring i rommet.\n" \
    "På østveggen er det en stor åpning."
    )
    else:
        print(rom8_utforsk_tekst)
        
    while True:

        valg = sjekk_gyldig_valg(spiller_prompt, gyldige_valg_i_rom["rom8"], ugyldig)

        if valg in ["hjelp", "utforsk", "tallkode", "lagre"]:
            hjelp_og_utforsk(valg, hjelp, rom8_utforsk_tekst, status)
            continue

        if valg == "nord":
            rom = "gang1"
            break
        elif valg == "øst":
            if status["åpen_ventil"]:
                rom = "rom4"
                break
            else:
                print(ugyldig)
        elif valg in ["ovn", "oljeovn"]:
            restart, rom = rom8_oljeovn(restart, status)
            if restart:
                break
        elif valg == "vifte":
            print("Du ser deg rundt etter noe å klatre på for å nå opp til viften, men finner ingenting. Kanskje like greit, skarpe, roterende, rustne vifter høres ikke så kjekt ut.")
        elif valg == "rør":
            print("Forskjellige rør strekker seg fra oljeovnen og opp til taket, antagelig på vei til å spre varme gjennom huset. Noen vibrerer smått, andre er ødelagte, alle er rustne.")
        elif valg == "oljekanner":
            print("Du plukker opp noen av oljekannene. De fleste er helt tomme, noen kjennes fulle ut, men en av dem har noe løst i seg.\n" \
                  "Du snur den opp ned og rister på den. En gammeldags nøkkel faller ut, som du plukker opp og legger i lommen.")
            status["falsk_nøkkel"] = True
        elif valg == "ventil":
            if not status["åpen_ventil"]:
                restart, rom = rom8_ventil(restart, status)
                if restart:
                    break
            else:
                print(ugyldig)
    return rom, restart, status, besøkt

# Funksjon for oljeovnen i rom 8
def rom8_oljeovn(restart, status):
    while True:
        if not status["har_brekkjern"]:
            print("Den gamle oljeovnen er fremdeles i bruk, og flammen sender varme ut til rommene i huset gjennom rør.\n" \
                  "Dersom du hadde hatt et verktøy eller et brekkjern kunne du relativt enkelt ødelagt ovnen.")
        else:
            svar = input("Den gamle oljeovnen er fremdeles i bruk, og flammen sender varme ut til rommene i huset gjennom rør.\n" \
                         "Vil du prøve å ødelegge ovnen med brekkjernet ditt? (ja/nei)").strip().lower()
            if svar == "ja":
                restart, rom = tap_restart("Du tar frem brekkjernet og ser etter et sted på oljeovnen å bryte opp.\n" \
                "Du bestemmer deg for en liten glipe skapt av rust langs toppen av oljeovnen. Du presser brekkjernet inn og legger vekten din på det til du kjenner at det gir etter.\n" \
                "Du får ikke egentlig med deg hva som skjer. Rommet lyser plutselig opp, og et lite øyeblikk kjenner du en intens varme i ansiktet før det går i sort for deg.")
                return restart, rom
            elif svar == "nei":
                return False, "rom8" 
            else:
                print(ugyldig)


# Funksjon for ventil i rom 8
def rom8_ventil(restart, status):
    while True:
        if not status["har_brekkjern"]:
            print("Du undersøker den rustne ventilen på østveggen og prøver å dannet kart i hodet ditt for å finne ut hva som er på andre siden.\n" \
                  "Til tross for rusten klarer du ikke å rive den ut av veggen. Kanskje om du hadde noe kraftigere å bruke.")
        else:
            svar = input("Du undersøker den rustne ventilen på østveggen og prøver å dannet kart i hodet ditt for å finne ut hva som er på andre siden.\n" \
                         "Vil du forsøke å fjerne ventilen med brekkjernet? (ja/nei)")
            if svar == "ja":
                print("Du presser brekkjernet inn i en glipe på den ene siden av ventilen og røsker godt til.\n" \
                      "Ventilen faller i gulvet med et voldsomt smell, og på den andre siden ser du et rom med en trapp.")
                status["åpen_ventil"] = True
                return False, "rom8"
            elif svar == "nei":
                return False, "rom8"
            else:
                print(ugyldig)