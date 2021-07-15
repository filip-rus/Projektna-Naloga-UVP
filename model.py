import random

STEVILO_DOVOLJENIH_NAPAK = 3
PRAVILNO = '+'
PONOVLJENO = 'o'
NAPACNO = '-'
ZMAGA = 'W'
PORAZ = 'X'
ZACETEK = 'S'

Evropa = [["SLOVENIJA","link_slovenija"],["AVSTRIJA","link_avstrija"],["ITALIJA","link_italija"]]
# test = Kviz("SLOVENIJA","link_slovenija",Evropa,[],[])

class Kviz:
    def __init__(self,geslo,povezava,celina,pravilni=None,ugib=None):
        self.geslo = geslo
        self.povezava = povezava
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
        return Kviz(self.celina[x][0],self.celina[x][1],self.celina,self.pravilni,[])

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
            self.ugib.append(beseda)
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

def nova_igra(celina):
    random.shuffle(celina)
    return Kviz(celina[0][0],celina[0][1],celina)
