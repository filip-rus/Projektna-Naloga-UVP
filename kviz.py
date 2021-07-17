import bottle 
import model

kviz = model.Kviz()

@bottle.get("/")
def index():
    return bottle.template("index.tpl")

@bottle.post("/<kontinent>/")
def nova_igra(kontinent):
    id_igre = kviz.nova_igra(kontinent)
    bottle.redirect("/{prva}/{druga}/".format(prva=kontinent,druga=id_igre))


@bottle.get("/<kontinent>/<id_igre:int>/")
def pokazi_igro(kontinent,id_igre):
    igra, stanje = kviz.igre[id_igre]
    return bottle.template("igra.tpl",igra=igra,kontinent=kontinent,id_igre=id_igre,stanje = stanje)

@bottle.post("/<kontinent>/<id_igre:int>/")
def ugibaj(kontinent,id_igre):
    beseda = bottle.request.forms.getunicode("beseda")
    kviz.ugibaj(id_igre,beseda)
    bottle.redirect("/{prva}/{druga}/".format(prva=kontinent,druga=id_igre))

@bottle.get("/img/<picture>")
def serve_pictures(picture):
    return bottle.static_file(picture, root="img")

bottle.run(reloader=True, debug=True)