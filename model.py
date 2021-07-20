import random
from timeit import default_timer as timer
import json

STEVILO_DOVOLJENIH_NAPAK = 3
PRAVILNO = '+'
PONOVLJENO = 'o'
NAPACNO = '-'
ZMAGA = 'W'
PORAZ = 'X'
ZACETEK = 'Z'
KONTINENTI = ["AZIJA","AFRIKA","EUROPA","AMERIKA"]
TEZAVNOST = ["TEKMOVALNO","NETEKMOVALNO"]

class Igra:
    def __init__(self,geslo,povezava,celina=None,zacetek=None,kontinent=None,pravilni=None,ugib=None):
        self.geslo = geslo
        self.povezava = povezava
        self.kontinent = kontinent
        if celina is None:
            self.celina = []
        else:
            self.celina = celina
        if zacetek is None:
            self.zacetek = 0
        else:
            self.zacetek = zacetek
        if ugib is None:
            self.ugib = []
        else:
            self.ugib = ugib
        if pravilni is None:
            self.pravilni = []
        else:
            self.pravilni = pravilni
    
    def napacen_poskus(self):
        return [ugib for ugib in self.ugib if ugib != self.geslo]

    def stevilo_napak(self):
        return len(self.napacen_poskus())

    def zamenjaj(self):
        for i,sez in enumerate(self.celina):
            if self.geslo in sez:
                x = i+1
            else:
                continue
        return Igra(self.celina[x][0],self.celina[x][1],self.celina,self.zacetek,self.kontinent,self.pravilni,[])

    def zmaga_posamezno(self):
        return self.geslo in self.ugib and self.stevilo_napak() < STEVILO_DOVOLJENIH_NAPAK
    
    def poraz(self):
        return STEVILO_DOVOLJENIH_NAPAK <= self.stevilo_napak()

    def zmaga(self):
        return len(self.pravilni) == len(self.celina) and self.stevilo_napak() < STEVILO_DOVOLJENIH_NAPAK

    def ugibaj(self,beseda):
        beseda = beseda.upper()
        if beseda in self.ugib:
            return PONOVLJENO
        elif beseda == self.geslo:
            self.pravilni.append(beseda)
            if self.zmaga():
                return ZMAGA
            else:
                return PRAVILNO
        else:
            self.ugib.append(beseda)
            if self.poraz():
                return PORAZ
            else:
                return NAPACNO

def preberi_celino(celina):
    celina = celina.upper()
    acc2 = []
    with open(celina+".txt",encoding='UTF-8') as d:
        for vrstica in d:
            vrstica = vrstica.strip()
            acc1 = vrstica.split("-")
            acc2.append(acc1)
    return acc2

def nova_igra(kontinent,tekmovalno):
    celina = preberi_celino(kontinent)
    random.shuffle(celina)
    if tekmovalno:
        zacetek = timer()
    else:
        zacetek = 0
    return Igra(celina[0][0],celina[0][1],celina,zacetek,kontinent.upper())


class Kviz:

    def __init__(self, datoteka_s_stanjem):
        self.igre = {}
        self.datoteka_s_stanjem = datoteka_s_stanjem
    
    def prost_id_igre(self):
        with open("stanje.json","r") as d:
            slovar = json.load(d)
            if len(slovar) == 0:
                return 0
            najvecji = float("-inf")
            for x in slovar.keys():
                if int(x) > najvecji:
                    najvecji = int(x)
                else:
                    continue
            return najvecji+1

    def nova_igra(self,kontinent,tekmovalno):
        id_igre = self.prost_id_igre()
        Kviz.zapis_zacetnega_stanja("stanje.json",id_igre)
        igra = nova_igra(kontinent,tekmovalno)
        self.igre[id_igre] = (igra,ZACETEK)
        return id_igre

    def ugibaj(self,id_igre,beseda,tekmovalno):
        igra, _ = self.igre[id_igre]
        stanje = igra.ugibaj(beseda)
        if stanje == PRAVILNO:
            igra = igra.zamenjaj()
        if stanje == ZMAGA:
            Kviz.zapis_koncnega_stanja("stanje.json",id_igre,igra.kontinent,igra.zacetek,tekmovalno)
        self.igre[id_igre] = (igra,stanje)

    @staticmethod
    def zapis_zacetnega_stanja(dat,id_igre):
        with open(dat,"r") as d:
            vsebina = json.load(d)
        vsebina[id_igre] = []
        vsebina[id_igre].append("nedokoncana")
        with open(dat,"w") as d:
                json.dump(vsebina,d)
    
    @staticmethod 
    def zapis_koncnega_stanja(dat,id_igre,celina,zacetek,tekmovalno):
        if tekmovalno:
            konec = timer()
            with open(dat,"r") as d:
                vsebina = json.load(d)
            vsebina[str(id_igre)][0]= "dokoncana"
            vsebina[str(id_igre)].append("tekmovalna")
            vsebina[str(id_igre)].append(konec-zacetek)
            vsebina[str(id_igre)].append(celina)
            with open("stanje.json","w") as d:
                json.dump(vsebina,d)
        else:
            with open("stanje.json","r") as d:
                vsebina = json.load(d)
            vsebina[str(id_igre)][0] = "dokoncana"
            vsebina[str(id_igre)].append("netekmovalna")
            with open("stanje.json","w") as d:
                json.dump(vsebina,d)


        