<!DOCTYPE html>
<html>

<body>

  <h1>Kviz držav sveta</h1>

  <p>
  Kviz držav sveta je najboljši kviz za preganjanje dolgčasa (poleg vislic).
  </p>

  <img src="/img/lems.jpg" alt="sani" 
  style="width:800px;height:400px;">

  <p>
  Vaši najboljši dosežki so: {{statistika_uporabnika}}
  </p>
  <p>
  Najboljši dosežki vseh uporabnikov so: {{statistika_vseh}}
  </p>

  <form action="/europa/" method="get">
    <button type="submit">Europa</button>
  </form>
  <br>
  <form action="/azija/" method="get">
    <button type="submit">Azija</button>
  </form>
  <br>
  <form action="/afrika/" method="get">
    <button type="submit">Afrika</button>
  </form>
  <br>
  <form action="/amerika/" method="get">
    <button type="submit">Amerika</button>
  </form>
  <br>
  <form action="/odjava/" method="post">
    <button type="submit">odjava</button>
  </form>
  %end
</body>

</html>