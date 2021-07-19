import bottle 
import model

kviz = model.Kviz()
SKRIVNOST = "moja skrivnost"


@bottle.get("/")
def index():
    return bottle.template("index.tpl")

@bottle.post("/<kontinent>/")
def nova_igra(kontinent):
    id_igre = kviz.nova_igra(kontinent)
    bottle.response.set_cookie('idigre', 'idigre{}'.format(id_igre), secret=SKRIVNOST, path='/')
    bottle.redirect("/{prva}/igra/".format(prva=kontinent))


@bottle.get("/<kontinent>/igra/")
def pokazi_igro(kontinent):
    if kontinent.upper() in model.KONTINENTI:
        id_igre = int(bottle.request.get_cookie('idigre', secret=SKRIVNOST).split('e')[1])
        igra, stanje = kviz.igre[id_igre]
        return bottle.template("igra.tpl",igra=igra,kontinent=kontinent,stanje = stanje)
    else:
        bottle.redirect("/")

@bottle.post("/<kontinent>/igra/")
def ugibaj(kontinent):
    id_igre = int(bottle.request.get_cookie('idigre', secret=SKRIVNOST).split('e')[1])
    beseda = bottle.request.forms.getunicode("beseda")
    kviz.ugibaj(id_igre,beseda)
    bottle.redirect("/{prva}/igra/".format(prva=kontinent))

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