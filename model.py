import random

STEVILO_DOVOLJENIH_NAPAK = 2
PRAVILNO = '+'
PONOVLJENO = 'o'
NAPACNO = '-'
ZMAGA = 'W'
PORAZ = 'X'
ZACETEK = 'Z'


class Igra:
    def __init__(self,geslo,povezava,celina=None,pravilni=None,ugib=None):
        self.geslo = geslo
        self.povezava = povezava
        if celina is None:
            self.celina = []
        else:
            self.celina = celina
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
        return Igra(self.celina[x][0],self.celina[x][1],self.celina,self.pravilni,[])

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

def nova_igra(celina):
    celina = preberi_celino(celina)
    random.shuffle(celina)
    return Igra(celina[0][0],celina[0][1],celina)


class Kviz:

    def __init__(self):
        self.igre = {}

    def prost_id_igre(self):
        if len(self.igre) == 0:
            return 0
        else:
            return max(self.igre.keys())+1

    def nova_igra(self,celina):
        id_igre = self.prost_id_igre()
        igra = nova_igra(celina)
        self.igre[id_igre] = (igra,ZACETEK)
        return id_igre

    def ugibaj(self,id_igre,beseda):
        igra, _ = self.igre[id_igre]
        stanje = igra.ugibaj(beseda)
        self.igre[id_igre] = (igra,stanje)


        