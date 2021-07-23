import bottle 
import model
import json

SKRIVNOST = "moja skrivnost"
DATOTEKA_S_STANJEM = 'stanje.json'

kviz = model.Kviz(DATOTEKA_S_STANJEM)
def zapisi_uporabnika(id,dat,ime):
    with open(dat,"r") as d:
        vsebina = json.load(d)
    vsebina[str(id)].insert(0,ime) 
    with open(dat,"w") as d:
        json.dump(vsebina,d)


@bottle.get("/")
def index():
    uporabnisko_ime = bottle.request.get_cookie("uporabnisko_ime")
    if uporabnisko_ime:
        statistika_uporabnika = model.statistika_uporabnika(uporabnisko_ime)
        statistika_vseh = model.statistika_vseh()
        return bottle.template("index.tpl",statistika_uporabnika=statistika_uporabnika,statistika_vseh=statistika_vseh)
    else:
        bottle.redirect("/prijava/")
    
@bottle.get("/prijava/")
def prijava_get():
    return bottle.template("prijava.tpl")

@bottle.post("/prijava/")
def prijava_post():
    uporabnisko_ime = bottle.request.forms.getunicode("uporabnisko_ime")
    bottle.response.set_cookie("uporabnisko_ime",uporabnisko_ime,path="/")
    bottle.redirect("/")

@bottle.post("/odjava/")
def odjava_post():
    bottle.response.delete_cookie("uporabnisko_ime",path="/")
    bottle.redirect("/")

@bottle.get("/<kontinent>/")
def tip(kontinent):
    return bottle.template("tezavnost.tpl",kontinent=kontinent)

@bottle.post("/<kontinent>/<tezavnost>/")
def nova_igra(kontinent,tezavnost):
    uporabnisko_ime = bottle.request.get_cookie("uporabnisko_ime")
    if tezavnost == "netekmovalno":
        id_igre = kviz.nova_igra(kontinent,False)
    elif tezavnost == "tekmovalno":
        id_igre = kviz.nova_igra(kontinent,True)
    else:
        bottle.redirect("/")
    zapisi_uporabnika(id_igre,"stanje.json",uporabnisko_ime)
    bottle.redirect("/{prva}/{druga}/igra/{tretja}/".format(prva=kontinent,druga=tezavnost,tretja=id_igre))

@bottle.get("/<kontinent>/<tezavnost>/igra/<id_igre>/")
def pokazi_igro(kontinent,tezavnost,id_igre):
    if kontinent.upper() in model.KONTINENTI and tezavnost.upper() in model.TEZAVNOST:
        igra, stanje = kviz.igre[int(id_igre)]
        return bottle.template("igra.tpl",igra=igra,kontinent=kontinent,stanje = stanje,tezavnost=tezavnost,id_igre=id_igre)
    else:
        bottle.redirect("/")

@bottle.post("/<kontinent>/<tezavnost>/igra/<id_igre>/")
def ugibaj(kontinent,tezavnost,id_igre):
    beseda = bottle.request.forms.getunicode("beseda")
    if tezavnost == "tekmovalno":
        kviz.ugibaj(id_igre,beseda,True)
    else:
        kviz.ugibaj(id_igre,beseda,False)
    bottle.redirect("/{prva}/{druga}/igra/{tretja}/".format(prva=kontinent,druga=tezavnost,tretja=id_igre))

@bottle.get("/img/<kontinent>/<picture>")
def serve_pictures(picture,kontinent):
    return bottle.static_file(picture, root="img/{prva}/".format(prva=kontinent))

@bottle.get("/img/<picture>")
def serve_pictures(picture):
    return bottle.static_file(picture, root="img")

@bottle.error(404)
def error_404(er):
    return "404 stran ne obstaja!"

@bottle.error(405)
def error_405(er):
    return "405 metoda ni dovoljena!"

@bottle.error(500)
def error_500(er):
    return "500 napaka na strežniku!"

bottle.run(reloader=True, debug=True)