import bottle 
import model

SKRIVNOST = "moja skrivnost"
DATOTEKA_S_STANJEM = 'stanje.json'

kviz = model.Kviz(DATOTEKA_S_STANJEM)


@bottle.get("/")
def index():
    return bottle.template("index.tpl")

@bottle.get("/<kontinent>/")
def tip(kontinent):
    return bottle.template("tezavnost.tpl",kontinent=kontinent)

@bottle.post("/<kontinent>/<tezavnost>/")
def nova_igra(kontinent,tezavnost):
    if tezavnost == "netekmovalno":
        id_igre = kviz.nova_igra(kontinent,False)
    elif tezavnost == "tekmovalno":
        id_igre = kviz.nova_igra(kontinent,True)
    else:
        bottle.redirect("/")
    bottle.response.set_cookie('idigre', 'idigre{}'.format(id_igre), secret=SKRIVNOST, path='/')
    bottle.redirect("/{prva}/{druga}/igra/".format(prva=kontinent,druga=tezavnost))

@bottle.get("/<kontinent>/<tezavnost>/igra/")
def pokazi_igro(kontinent,tezavnost):
    if kontinent.upper() in model.KONTINENTI and tezavnost.upper() in model.TEZAVNOST:
        id_igre = int(bottle.request.get_cookie('idigre', secret=SKRIVNOST).split('e')[1])
        igra, stanje = kviz.igre[id_igre]
        return bottle.template("igra.tpl",igra=igra,kontinent=kontinent,stanje = stanje,tezavnost=tezavnost,id_igre=id_igre)
    else:
        bottle.redirect("/")

@bottle.post("/<kontinent>/<tezavnost>/igra/")
def ugibaj(kontinent,tezavnost):
    id_igre = int(bottle.request.get_cookie('idigre', secret=SKRIVNOST).split('e')[1])
    beseda = bottle.request.forms.getunicode("beseda")
    if tezavnost == "tekmovalno":
        kviz.ugibaj(id_igre,beseda,True)
    else:
        kviz.ugibaj(id_igre,beseda,False)
    bottle.redirect("/{prva}/{druga}/igra/".format(prva=kontinent,druga=tezavnost))

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