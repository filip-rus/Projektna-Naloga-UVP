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

  <a href="/europa/">
  <button type="submit">Europa</button>
  </a>
  <br><br>
  <a href="/azija/">
  <button type="submit">Azija</button>
  </a>
  <br><br>
  <a href="/afrika/">
  <button type="submit">Afrika</button>
  </a>
  <br><br>
  <a href="/amerika/">
  <button type="submit">Amerika</button>
  </a>
  <br><br>
  <form action="/odjava/" method="post">
    <button type="submit">odjava</button>
  </form>
   
</body>

</html>