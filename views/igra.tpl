% import model
% import json

<!DOCTYPE html>
<html>

<body>
  

% if stanje == model.ZMAGA and tezavnost.upper()=="TEKMOVALNO":
%with open("stanje.json","r") as d:
%  vsebina = json.load(d)
%cas = vsebina[str(id_igre)][4]
%end
  <h1>ZMAGA</h1>
  <p>Zmagali ste, potrebovali ste {{cas}} sekunde!</p>
  <br>
  <form action="/">
    <button type="submit">Zacetna stran</button>
  </form>
  <br>
  <form action="/{{kontinent}}/" method="get">
    <button type="submit">Ponovna igra</button>
  </form>
%elif stanje == model.ZMAGA:
  <h1>ZMAGA</h1>
  <p>Zmagali ste!</p>
  <br>
  <form action="/">
    <button type="submit">Zacetna stran</button>
  </form>
  <br>
  <form action="/{{kontinent}}/" method="get">
    <button type="submit">Ponovna igra</button>
  </form>

% elif stanje == model.PORAZ:
  <h1>PORAZ</h1>
  <p>Izgubili ste!</p>
  <form action="/">
    <button type="submit">Zacetna stran</button>
  </form>
  <br>
  <form action="/{{kontinent}}/" method="get">
    <button type="submit">Ponovna igra</button>
  </form>


% else:
<h1>{{kontinent.upper()}},{{igra.geslo}}</h1>
  <img src="/img/{{kontinent+"/"+igra.povezava}}" alt="zastava"
  style="width:850px;height:650px;">
  <br>
  <br>
  <form action="/{{kontinent}}/{{tezavnost}}/igra/{{id_igre}}/" method="post">
    Država: <input type="text" name="beseda" autofocus autocomplete="off">
    <button type="submit">Vnesi</button>
  %if tezavnost.upper() == "NETEKMOVALNO":
  </form>
  %if len(igra.ugib) >= 2:
<details>
  <summary>Odgovor</summary>
  <p>{{igra.geslo.lower().capitalize()}}</p>
</details>
%end
%end
%end

</body>

</html>