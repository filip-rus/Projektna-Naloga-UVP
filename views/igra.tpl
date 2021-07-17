% import model

<!DOCTYPE html>
<html>

<body>

  

% if stanje == model.ZMAGA:
  <h1>ZMAGA</h1>
  <p>Zmagali ste!</p>
  <br>
  <form action="/">
    <button type="submit">Zacetna stran</button>
  </form>
  <br>
  <form action="/{{kontinent}}/" method="post">
    <button type="submit">Ponovna igra</button>
  </form>

% elif stanje == model.PORAZ:
  <h1>PORAZ</h1>
  <p>Izgubili ste!</p>
  <form action="/">
    <button type="submit">Zacetna stran</button>
  </form>
  <br>
  <form action="/{{kontinent}}/" method="post">
    <button type="submit">Ponovna igra</button>
  </form>


% else:
<h1>{{kontinent.upper()}}</h1>
  <img src={{igra.povezava}} alt="zastava"
  style="width:300px;height:200px;">

  <form action="/{{kontinent}}/{{id_igre}}/" method="post">
    Država: <input type="text" name="beseda" />
    <button type="submit">Vnesi</button>
  </form>
%end

</body>

</html>