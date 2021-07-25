import random
konst ="abcdefghijklmnoprstuvzqwyx1234567890"
def veliko(vhod,izhod):
    with open(izhod,"w",encoding="utf-8") as f:
        with open(vhod,"r",encoding="utf-8") as d:
            for vrstica in d:
                vrstica = vrstica.upper()
            
                f.write(vrstica)

veliko("AMERIKA.txt","velike.txt")

def link(dat):
    konst ="abcdefghijklmnoprstuvzqwyx1234567890"
    niz = ""
    with open(dat,"w",encoding="utf-8") as d:
        for i in range(60):
            while len(niz) < 8:
                niz += konst[random.randrange(len(konst))]
            d.write("-"+niz+".png"+"\n")
            niz = ""

link("izhodna.txt")

import json

