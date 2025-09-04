# Fil som inneholder alle rommene.

import engine

# Funksjon for rom1
def rom1(rom, restart, besøkt):
    besøkt = engine.rombeskrivelse("rom1", engine.rom1_inngang_tekst, engine.rom1_utforsk_tekst, besøkt)

    while True: 
        verb, obj = engine.parse_kommando()

        if verb in ["hjelp", "utforsk", "tallkode", "lagre"]:
            engine.hjelp_og_utforsk(verb, engine.hjelp, engine.rom1_utforsk_tekst, engine.status)
            continue

        elif verb == "gå":
            if obj == "øst":
                rom = "rom2"
                break
            else:
                print(engine.ingen_vei)
                break

        elif verb == "se":
            if obj == "vindu":
                valg = input("Stigen under vinduet ser solid ut. Vil du forsøke å klatre? (ja/nei) ").strip().lower()
                if valg == "ja":
                    restart, rom = engine.tap_restart(
                        "Du klatrer stigen opp mot vinduet. "
                        "Idet du når toppen, knekker den sammen under deg. "
                        "Du faller på nakken og alt går umiddelbart i svart."
                    )
                    break
                elif valg == "nei":
                    break
                else:
                    print(engine.ugyldig)

        elif verb == "bruk" and isinstance(obj, tuple):
            item, target = obj
            if item == "brekkjern" and target == "vindu":
                print("Du prøver å bruke brekkjernet på vinduet, men det sitter for hardt.")
            # Andre kombinasjoner går her.
            else:
                print(f"Kan ikke bruke {item} på {target}, men det fungerer ikke her.")

    return rom, restart, besøkt

# Funksjon for rom2
def rom2(rom, restart, status, besøkt):
    besøkt = engine.rombeskrivelse("rom2", engine.rom2_inngang_tekst, engine.rom2_utforsk_tekst, besøkt)

    while True:  
        verb, obj = engine.parse_kommando()

        if verb in ["hjelp", "utforsk", "tallkode", "lagre"]:
            engine.hjelp_og_utforsk(verb, engine.hjelp, engine.rom2_utforsk_tekst, status)
            continue
        
        if verb == "gå":
            if obj == "nord":
                rom = "rom3"
                break
            elif obj == "øst":
                restart, rom = rom2_ost(restart)
                if restart:
                    break
            else:
                print(engine.ingen_vei)

        elif verb == "se":
            if obj == "skap":
                if not status["rom2_skap"]:
                    print("Du åpner skapdørene, og støkker idet et rustent strykebrett faller over deg.\nEtter at nervene roer seg kikker du rundt i skapet, men ser ingenting av interesse.")
                    status["rom2_skap"] = True
                else:
                    print("Vaskebrettet ligger på gulvet, resten av skapet er uinteressant.")
            elif obj == "arbeidsbenk":
                status = rom2_arbeidsbenk(status)
            elif obj == "hammer" and not status["har_hammer"]:
                print("En gammel, rusten hammer.")
            else:
                print(engine.ugyldig)

        elif verb == "ta":
            if obj == "hammer" and not status["har_hammer"]:
                print("Idet du plukker opp hammeren, smuldrer treskaftet opp...")
                status["har_hammer"] = True
            else:
                print(engine.ugyldig)

        elif verb == "bruk":
            if engine.har_gjenstand(obj):
                print(engine.bruk_feilmelding(obj))
            else:
                print(engine.not_objekt)
                
        else:
            print(engine.ugyldig)
    return rom, restart, status, besøkt

# Funksjon for arbeidsbenken i rom2
def rom2_arbeidsbenk(status):
    if not status["har_hammer"]:
        print("Arbeidsbenken består av relativt råttent treverk. Det ligger en hammer på den ene siden.")
    else:
        print("Arbeidsbenken består av relativt råttent treverk.")
    return status

# Funksjon for å velge øst i rom 2
def rom2_ost(restart):
    while True:
        svar = input("Etterhvert som du nærmer deg døren på østveggen hører du bevegelse og noe som høres ut som grynting på andre siden av døren. Vil du åpne den? (ja/nei) ").lower().strip()
        if svar == "ja":
            restart, rom = engine.tap_restart(engine.tap)
            return restart, rom
        elif svar == "nei":
            return False, "rom2"
        else:
            print(engine.ugyldig)

# Funksjon for rom 3
def rom3(rom, restart, status, besøkt):
    besøkt = engine.rombeskrivelse("rom3", engine.rom3_inngang_tekst, engine.rom3_utforsk_tekst, besøkt)

    while True:  
        verb, obj = engine.parse_kommando()

        if verb in ["hjelp", "utforsk", "tallkode", "lagre"]:
            engine.hjelp_og_utforsk(verb, engine.hjelp, engine.rom3_utforsk_tekst, status)
            continue
        
        if verb == "gå":
            if obj == "sør":
                rom = "rom2"
                break
            elif obj == "vest":
                rom = "rom4"
                break
            elif obj == "nord":
                rom = "gang1"
                break
            else:
                print(engine.ingen_vei)

        elif verb in ["se", "ta"]:
            if obj == "malingsspann":
                status = rom3_malingsspann(status, verb)
            elif obj == "bokser":
                print("En haug med det som ser ut til å en gang ha vært pappesker, alle merket med tallet '4', men er nå en haug med forråtnende papp.")
                status["tall1"] = True
            else:
                print(engine.ugyldig)

        elif verb == "bruk" and isinstance(obj, tuple):
            item, target = obj

            if item not in engine.inventar or not engine.inventar[item]:
                print(f"Du har ikke {item} i inventaret.")
                continue

            if item == "brekkjern" and target == "malingsspann":
                if not engine.inventar["har_nøkkel"]:
                    print(
                        "Du bruker det lille brekkjernet du fant til å åpne malingsspannet som hadde noe inni seg.\n"
                        "Inni finner du en gammeldags nøkkel!"
                    )
                    engine.inventar["har_nøkkel"] = True
                else:
                    print("Malingsspannene er tomme nå.")
            else:
                print("Det ser ikke ut til å fungere her.")

        else:
            print(engine.ugyldig)
    return rom, restart, status, besøkt

# Funksjon for malingsspann i rom 3
def rom3_malingsspann(status, verb):
    if verb == "se":
        if not engine.inventar["har_nøkkel"]:
            print("En haug med gamle malingsspann.")
        else:
            print("Et sett gamle malingsspann, men de er tomme nå.")

    elif verb == "ta":
        if not engine.inventar["har_nøkkel"]:
            print(
                "Du plukker opp noen av malingsspannene, og hører noe løst inni et av dem.\n"
                "Du forsøker å åpne det, men inntørket maling og rust har gjort det nesten umulig."
            )
        else:
            print("Du rister på noen av de uåpnede malingsspannene, men hører ingenting.") 

    return status

# Funksjon for rom4
def rom4(rom, restart, status, besøkt):
    if not besøkt["rom4"]:
        print(engine.rom4_inngang_tekst)
        besøkt["rom4"] = True

    if status["åpen_ventil"]:
        print("I midten av rommet står en trapp opp til etasjen over. Du ser en dør i enden av trappen.\n" \
    "Under trappen står et gammelt skrivebord med en stol. På vestveggen er det et åpent hull.\n"
    "Der er en åpning på østveggen."
    )
    else:
        print(engine.rom4_utforsk_tekst)
        
    while True:
        verb, obj = engine.parse_kommando()

        if verb in ["hjelp", "utforsk", "tallkode", "lagre"]:
            engine.hjelp_og_utforsk(verb, engine.hjelp, engine.rom3_utforsk_tekst, status)
            continue
        
        elif verb == "gå":
            if obj == "vest":
                if status["åpen_ventil"]:
                    rom = "rom8"
                    break
                else:
                    print(engine.ingen_vei)
            elif obj == "øst":
                rom = "rom3"
                break
            elif obj == "dør":
                print("Du klatrer opp den morkne trappa og vrir om håndtaket på døren.\n"
                "Samme hvor hardt du prøver, lar den ikke bevege på seg. Du merker et gammeldags nøkkelhull under håndtaket.")
            else:
                print(engine.ingen_vei)

        elif verb == "se":
            if obj == "ventil":
                if not status["åpen_ventil"]:
                    print("En stor ventil er plassert midt på vestveggen. Det kommer varm luft fra den andre siden.")
                else:
                    print(engine.ugyldig)
            elif obj == "trapp":
                print("En gammel, morken trapp. Du ser en dør i toppen av trappen.")
            elif obj == "dør":
                print("En gammel dør. Den har et gammeldags nøkkelhull under håndtaket.")
            elif obj == "skrivebord":
                if engine.inventar["brekkjern"]:
                    print("Et gammelt og godt brukt skrivebord med noen tomme skuffer.")
                else:
                    print("Det som uten tvil var et vakkert møbel en gang er nå slitt og råtnende. "
                    "Alle skuffene mangler utenom én, men den er låst med en 3-sifret hengelås. ")
            elif obj == "hengelås":
                if engine.status["hengelås"]:
                    print("Den åpne hengelåsen ligger på skrivebordet.")
                    continue
                while True:
                    kode_input = input("En gammel 3-sifret hengelås. Tast inn koden eller skriv 'avbryt': "
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
                        engine.inventar["brekkjern"] = True
                        engine.status["hengelås"] = True
                        break
                    else:
                        print("Feil kode. Prøv igjen.")

        elif verb == "bruk" and isinstance(obj, tuple):
            item, target = obj
            if item == "nøkkel" and target == "dør":
                if engine.inventar["falsk_nøkkel"]:
                    restart, rom = engine.tap_restart("Med litt makt klarer du å presse nøkkelen du fant inn i nøkkelhullet.\n"
                    "Du rister litt i nøkkelen i et forsøk på å vri den rundt, men nøkkelen knekker. Plutselig uler en alarm gjennom kjelleren.\n"
                    "Du hører en rytmisk dundring som blir høyere, og et gutturalt rop. Du rekker knapt å snu deg for å se inn i et fettete, kvisete ansikt før alt går i sort.")
                    return restart, rom
                elif engine.inventar["har_nøkkel"]:
                    print("Du klatrer opp til døren i toppen av trappen, og setter den gamle nøkkelen i nøkkelhullet.\n"
                    "Du hører et tydelig *klikk* når du vrir den. Med noe makt klarer du å vri om håndtaket, åpne døren, og rømme ut av kjelleren.\n"
                    "Gratulerer! Du har unngått Kjellerbeistet og rømt fra kjelleren!")
                while True:
                    valg_restart = input(engine.omstart).strip().lower()
                    if valg_restart == "ja":
                        return True, "rom1" 
                    elif valg_restart == "nei":
                        quit()
                    else:
                        print(engine.ugyldig)

        else:
            print(engine.ugyldig)
    return rom, restart, status, besøkt

# Funksjon for gang1
def gang1(rom, restart, status, besøkt):
    besøkt = engine.rombeskrivelse("gang1", engine.gang1_inngang_tekst, engine.gang1_utforsk_tekst, besøkt)

    while True:  
        verb, obj = engine.parse_kommando()

        if verb in ["hjelp", "utforsk", "tallkode", "lagre"]:
            engine.hjelp_og_utforsk(verb, engine.hjelp, engine.rom2_utforsk_tekst, status)
            continue
        
        if verb == "gå":
            if obj == "sør":
                rom = "rom3"
                break 
            elif obj == "nordvest":
                rom = "rom6"
                break 
            elif obj == "nordøst":
                rom = "rom5"
                break 
            elif obj == "sørøst":
                rom = "rom7"
                break 
            elif obj == "sørvest":
                rom = "rom8"
                break 
            else:
                print(engine.ingen_vei)
                
        else:
            print(engine.ugyldig)
    return rom, restart, status, besøkt

# Funksjon for rom5
def rom5(rom, restart, status, besøkt):
    besøkt = engine.rombeskrivelse("rom5", engine.rom5_inngang_tekst, engine.rom5_utforsk_tekst, besøkt)
    while True:  # Løkke for rom5

        valg = engine.sjekk_gyldig_valg(engine.spiller_prompt, engine.gyldige_valg_i_rom["rom5"], engine.ugyldig)

        if valg in ["hjelp", "utforsk", "tallkode", "lagre"]:
            engine.hjelp_og_utforsk(valg, engine.hjelp, engine.rom5_utforsk_tekst, status)
            continue

        if valg == "sør":
            rom = "gang1"
            break  # gå videre til gang
        elif valg in ["esker", "kasser"]:
            print("Du ser over stablene av esker som står spredd langs veggene, i varierende grad av forråtnelse.\n" \
            "Du åpner noen vilkårlige esker, og finner noen fylt med gamle tegneserier, andre med gamle spill, og underlig nok en tredje full av flasker fylt med en gul væske.")
        elif valg == "reoler":
            print("Du går frem og tilbake i rommet og saumfarer hyllene etter noe nyttig.\n" \
            "På noen av hyllene står det noen gamle lekefigurer, men du finner ingenting av nytte.")
        elif valg == "skap":
            print("Bakerst i rommet står det et skap som minner deg om skoledagene dine. Sett bort fra tallet '7' på forsiden er det ingenting uvanlig med det.\n" \
            "Du tar tak i håndtaket og røsker til, men skapet beveger seg ikke.")
            status["tall2"] = True
        elif valg in ["hylle", "hyller"]:
            restart, rom = rom5_hylle(status)
        elif valg == "øst":
            if status["åpen_hylle"]:
                rom = "rom10"
                break
            else:
                print(engine.ugyldig)
    return rom, restart, status, besøkt

# Funksjon for hylle i rom5
def rom5_hylle(status):
    while True:
        svar = input("Du undersøker hyllen på østveggen litt nærmere, og merker en underlig lukt fra dem. Ved nærmere undersøkelse ser du en dør bak hyllen. Vil du forsøke å flytte på den? ").strip().lower()
        if svar == "ja":
            print("Du dytter så hardt du kan i siden av hyllen, som etterhvert begynner å skli til siden. Bak finner du en åpenbart hjemmesnekret dør.")
            status["åpen_hylle"] = True
            engine.rom5_utforsk_tekst = ("Du finner deg omringet av høye stabler av kasser og esker. To høye reoler står midt i rommet, og langs den bakre veggen står et enkelt skap. Dører leder sør og øst."
            )
            return status
        elif svar == "nei":
            return False, "rom6" 
        else:
            print(engine.ugyldig)

# Funksjon for rom6
def rom6(rom, restart, status, besøkt):
    besøkt = engine.rombeskrivelse("rom6", engine.rom6_inngang_tekst, engine.rom6_utforsk_tekst, besøkt)
    while True: 

        valg = engine.sjekk_gyldig_valg(engine.spiller_prompt, engine.gyldige_valg_i_rom["rom6"], engine.ugyldig)

        if valg in ["hjelp", "utforsk", "tallkode", "lagre"]:
            engine.hjelp_og_utforsk(valg, engine.hjelp, engine.rom6_utforsk_tekst, status)
            continue

        if valg == "sør":
            rom = "gang1"
            break
        elif valg == "nord":
            rom = "rom9"
            break
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
            restart, rom = engine.tap_restart("Med noe makt klarer du å vri om på hjulet. Det begynner umiddelbart å fosse vann ut av vaskemaskinene, og et gitter smeller ned foran døren.\n" \
            "Du prøver desperat å snu hjulet tilbake, men det sitter låst fast. Du forsøker å rive opp gitteret, men det rikker seg ikke.\n" \
            "Det tar bare noen sekunder før rommet er fylt med vann. Uten luft svelger du ned vann, og alt går i sort.")
            return restart, rom
        elif svar == "nei":
            return False, "rom6" 
        else:
            print(engine.ugyldig)

# Funksjon for rom 7 - monsterkjelleren
def rom7(rom, restart, status, besøkt):
    besøkt = engine.rombeskrivelse("rom7", engine.rom7_inngang_tekst, engine.rom7_utforsk_tekst, besøkt)
    while True:

        valg = engine.sjekk_gyldig_valg(engine.spiller_prompt, engine.gyldige_valg_i_rom["rom7"], engine.ugyldig)

        if valg in ["hjelp", "utforsk", "tallkode", "lagre"]:
            engine.hjelp_og_utforsk(valg, engine.hjelp, engine.rom7_utforsk_tekst, status)
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
    besøkt = engine.rombeskrivelse("rom8", engine.rom8_inngang_tekst, engine.rom8_utforsk_tekst, besøkt)
    while True: 

        valg = engine.sjekk_gyldig_valg(engine.spiller_prompt, engine.gyldige_valg_i_rom["rom8"], engine.ugyldig)

        if valg in ["hjelp", "utforsk", "tallkode", "lagre"]:
            engine.hjelp_og_utforsk(valg, engine.hjelp, engine.rom8_utforsk_tekst, status)
            continue

        if valg == "nord":
            rom = "gang1"
            break
        elif valg == "øst":
            if status["åpen_ventil"]:
                rom = "rom4"
                break
            else:
                print(engine.ugyldig)
        elif valg in ["ovn", "oljeovn"]:
            restart, rom = rom8_oljeovn(restart, status)
            if restart:
                break
        elif valg == "vifte":
            print("Du ser deg rundt etter noe å klatre på for å nå opp til viften, men finner ingenting. Kanskje like greit, skarpe, roterende, rustne vifter høres ikke så kjekt ut.")
        elif valg == "rør":
            print("Forskjellige rør strekker seg fra oljeovnen og opp til taket, antagelig på vei til å spre varme gjennom huset. Noen vibrerer smått, andre er ødelagte, alle er rustne.")
        elif valg == "oljekanner":
            if not status["falsk_nøkkel"]:
                print("Du plukker opp noen av oljekannene. De fleste er helt tomme, noen kjennes fulle ut, men en av dem har noe løst i seg.\n" \
                  "Du snur den opp ned og rister på den. En gammeldags nøkkel faller ut, som du plukker opp og legger i lommen.")
                status["falsk_nøkkel"] = True
            else:
                print("Et par bulkete og sølete oljekanner.")
        elif valg == "ventil":
            if not status["åpen_ventil"]:
                restart, rom = rom8_ventil(restart, status)
                if restart:
                    break
            else:
                print(engine.ugyldig)
        elif valg == "sør":
            if not status["glødende_sopp"]:
                print("Du åpner døren som leder sør, men rommet er så mørkt at du ikke tør ta steget inn.")
            else:
                rom = "rom11"
    return rom, restart, status, besøkt

# Funksjon for oljeovnen i rom 8
def rom8_oljeovn(restart, status):
    while True:
        if not status["brekkjern"]:
            print("Den gamle oljeovnen er fremdeles i bruk, og flammen sender varme ut til rommene i huset gjennom rør.\n" \
                  "Dersom du hadde hatt et verktøy eller et brekkjern kunne du relativt enkelt ødelagt ovnen.")
            return False, "rom8"
        else:
            svar = input("Den gamle oljeovnen er fremdeles i bruk, og flammen sender varme ut til rommene i huset gjennom rør.\n" \
                         "Vil du prøve å ødelegge ovnen med brekkjernet ditt? (ja/nei)").strip().lower()
            if svar == "ja":
                restart, rom = engine.tap_restart("Du tar frem brekkjernet og ser etter et sted på oljeovnen å bryte opp.\n" \
                "Du bestemmer deg for en liten glipe skapt av rust langs toppen av oljeovnen. Du presser brekkjernet inn og legger vekten din på det til du kjenner at det gir etter.\n" \
                "Du får ikke egentlig med deg hva som skjer. Rommet lyser plutselig opp, og et lite øyeblikk kjenner du en intens varme i ansiktet før det går i sort for deg.")
                return restart, rom
            elif svar == "nei":
                return False, "rom8" 
            else:
                print(engine.ugyldig)


# Funksjon for ventil i rom 8
def rom8_ventil(restart, status):
    while True:
        if not status["har_brekkjern"]:
            print("Du undersøker den rustne ventilen på østveggen og prøver å dannet kart i hodet ditt for å finne ut hva som er på andre siden.\n" \
                  "Til tross for rusten klarer du ikke å rive den ut av veggen. Kanskje om du hadde noe kraftigere å bruke.")
            return False, "rom8"
        else:
            svar = input("Du undersøker den rustne ventilen på østveggen og prøver å dannet kart i hodet ditt for å finne ut hva som er på andre siden.\n" \
                         "Vil du forsøke å fjerne ventilen med brekkjernet? (ja/nei)")
            if svar == "ja":
                print("Du presser brekkjernet inn i en glipe på den ene siden av ventilen og røsker godt til.\n" \
                      "Ventilen faller i gulvet med et voldsomt smell, og på den andre siden ser du et rom med en trapp.")
                status["åpen_ventil"] = True
                engine.rom8_utforsk_tekst = ("Du står i det du bare kan anta er et gammeldags fyrrom basert på hva du har sett på film og TV. Midt i rommet står en gammel oljeovn.\n" \
                "I taket knirker en rusten vifte i vei, og flere rør går fra oljeovnen og opp til forskjellige punkter i taket. Oljekanner står rundt om kring i rommet.\n" \
                "På østveggen er det en stor åpning."
                )
                return False, "rom8"
            elif svar == "nei":
                return False, "rom8"
            else:
                print(engine.ugyldig)

# Funksjon for rom 9
def rom9(rom, restart, status, besøkt):
    besøkt = engine.rombeskrivelse("rom9", engine.rom9_inngang_tekst, engine.rom9_utforsk_tekst, besøkt)
    while True:

        valg = engine.sjekk_gyldig_valg(engine.spiller_prompt, engine.gyldige_valg_i_rom["rom9"], engine.ugyldig)

        if valg in ["hjelp", "utforsk", "tallkode", "lagre"]:
            engine.hjelp_og_utforsk(valg, engine.hjelp, engine.rom9_utforsk_tekst, status)
            continue

        if valg == "sør":
            rom = "rom6"
            break
        elif valg in ["sopp", "glødende sopp"]:
            print("Du tar tak i en av soppene og napper til. Gratulerer, du har en glødende sopp! Kanskje best å ikke smake på...")
            status["glødende_sopp"] = True
        elif valg == "bøtte":
            if not status["bøtte"]:
                print("Du nærmer deg bøtten og kjenner en underlig dunts som gjør det litt vanskelig å puste. Idet du forsøker å plukke den opp faller bunnen ut,\n" \
                "og innholdet flyter utover gulvet.")
                status["bøtte"] = True
            else:
                print("Gulvet er dekket av en mørk, klissete substans og bøtten ligger henslengt på siden.")
    
    return rom, restart, status, besøkt

# Funksjon for rom 10
def rom10(rom, restart, status, besøkt):
    besøkt = engine.rombeskrivelse("rom10", engine.rom10_inngang_tekst, engine.rom10_utforsk_tekst, besøkt)
    while True:

        valg = engine.sjekk_gyldig_valg(engine.spiller_prompt, engine.gyldige_valg_i_rom["rom10"], engine.ugyldig)

        if valg in ["hjelp", "utforsk", "tallkode", "lagre"]:
            engine.hjelp_og_utforsk(valg, engine.hjelp, engine.rom10_utforsk_tekst, status)
            continue

        if valg == "vest":
            rom = "rom5"
            break
        elif valg in ["aviser", "magasiner"]:
            print("Du ser kjapt gjennom stablene med aviser og magasiner, men uten å finne noe særlig av interesse. Med mindre du er interesert i Tysvær Bygdablad eller gamle utgaver av Autofil.")
        elif valg in ["bøker", "hyller"]:
            print("Bokhyllene og bøkene i dem er dekket av et tykt lag støv. Du blåser på noen av dem, og ser at det stort sett er 'Animorphs'-bøker.")
        elif valg == "pult":
            rom = rom10_pult(status)
            break

    return rom, restart, status, besøkt

# Funksjon for pult i rom 10
def rom10_pult(status):
    while True:         
        svar = input("På pulten ligger det en gammel pizzaeske, en manual og en haug med avisutklipp. Hva vil du gjøre? ")

        if svar == "pizzaeske":
            if not status["kart"]:
                print("Du blåser støvet av den gamle pizzaesken og plukker den opp. På undersiden ser du noe som ligner på et slags kart over kjelleren. Du river det løs og tar det med deg.")
                status["kart"] = True
            else:
                print("En pizzaeske med et hull hvor det tidligere var et kart.")
        elif svar == "manual":
            print("På den slitte gamle manualen står det i store bokstaver, 'OLJEOVN m.1977'. Du prøver å plukke den opp, men ombestemmer deg sidene begynner å falle ut.")
        elif svar == "avisutklipp":
            print("Du romsterer forsiktig gjennom haugen av avisutklipp. De fleste er gamle spillanmeldelser hvor terningkastet er skrablet over, men noen handler om rapporter om uvanlige lyder fra et nedslitt hus.")
        return status
    
# Funksjon for rom 11
def rom11(rom, restart, status, besøkt):
    besøkt = engine.rombeskrivelse("rom11", engine.rom11_inngang_tekst, engine.rom11_utforsk_tekst, besøkt)
    while True:

        valg = engine.sjekk_gyldig_valg(engine.spiller_prompt, engine.gyldige_valg_i_rom["rom11"], engine.ugyldig)

        if valg in ["hjelp", "utforsk", "tallkode", "lagre"]:
            engine.hjelp_og_utforsk(valg, engine.hjelp, engine.rom11_utforsk_tekst, status)
            continue

        if valg == "nord":
            rom = "rom8"
            break
        elif valg == "fotspor":
            print("Fotsporene leder frem og tilbake mellom luken og døren, og ser relativt ferske ut sammenlignet med resten av rommet.")
        elif valg == "luke":
            print("Luken er låst med ikke bare én, men tre hengelåser. To trenger en nøkkel, og den tredje trenger en 4-sifret kode. Du forsøker å dra i den, uten hell.")
        elif valg in ["skilt", "messingskilt"]:
            print("Du tørker litt støv og rusk av messingskiltet og leser det. 'ADGANG KUN FOR ALFAMENN!!'")

    return rom, restart, status, besøkt