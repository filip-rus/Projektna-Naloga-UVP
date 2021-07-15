import model

PONOVNI_ZAGON = "p"
IZHOD = "i"

def izpis_igre(igra):
    tekst = f"""############################\n
    Katera država je prikazana?\n
    {igra.povezava}\n
    ############################\n"""
    return tekst

def izpis_zmage(igra):
    tekst = f"""######################################\n
    Bravo! Zmagali ste!\n
######################################\n"""
    return tekst

def izpis_poraza(igra):
    tekst = f"""######################################\n
    Porabili ste vse poskuse.\n
    Pravilno geslo: {igra.geslo}\n
######################################\n"""
    return tekst

def zahtevaj_vnos(): 
    return input('Vnesite državo:')

def zahtevaj_moznost():
    return input('Vnesite možnost:')

def ponudi_moznosti():
    tekst = f""" Vpišite črko za izbor naslednjih možnosti:\n
    {PONOVNI_ZAGON} : ponovni zagon igre\n
    {IZHOD} : izhod\n
    """
    return tekst

def izberi_ponovitev():
    print(ponudi_moznosti())
    moznost = zahtevaj_moznost().strip().lower()
    if moznost == PONOVNI_ZAGON:
        igra = model.nova_igra(model.Evropa)
        print(izpis_igre(igra))
        return igra
    else:
        return IZHOD

def pozeni_vmesnik():
    igra = model.nova_igra(model.Evropa)
    print(izpis_igre(igra))
    while True:
        država = zahtevaj_vnos()
        odziv = igra.ugibaj(država)
        if odziv == model.ZMAGA:
            print(izpis_zmage(igra))
            igra = izberi_ponovitev()
            if igra == IZHOD:
                break
        elif odziv == model.PORAZ:
            print(izpis_poraza(igra))
            igra = izberi_ponovitev()
            if igra == IZHOD:
                break
        elif odziv == model.PRAVILNO:
            igra = igra.zamenjaj()
            print(izpis_igre(igra))
        else:
            print(izpis_igre(igra))


pozeni_vmesnik()