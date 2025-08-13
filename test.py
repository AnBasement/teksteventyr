# Fil som brukes for å gjøre endringer på hovedfilen uten å gjøre det direkte i programmet.

# Funksjon for rom4
def hjelp_og_utforsk(valg, hjelp_tekst, utforsk_tekst):
    if valg == "hjelp":
        print(hjelp_tekst)
    elif valg == "utforsk":
        print(utforsk_tekst)