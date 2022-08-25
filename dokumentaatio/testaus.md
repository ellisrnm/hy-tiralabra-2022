## Testausdokumentti

### Yksikkötestaus

Yksikkötestaukset toteutetaan ohjelmallisesti. Yksikkötestit voidaan suorittaa seuraavalla komennolla:

    pytest rsa

Yksikkötestauksen kattavuuden voi tarkistaa komennolla:

    coverage run --branch -m pytest

Kattavuudesta voi generoida HTML raportin index.html projektin hakemistoon htmlcov komennolla:

    coverage html

Lisäksi koodin laadun voi analysoida pylintilla komennolla:

    pylint rsa

Yksikkötestaukset suoritetaan automaattisesti myös jokaisen päähaaran muutosten julkaisun yhteydessä. Myös yksikkötestien kattavuus lasketaan samassa yhteydessä automaattisesti. Yksikkötestauksen kattavuusraportti löytyy [Codecovista](https://codecov.io/gh/ellisrnm/hy-tiralabra-2022).

Yksikkötesteillä on testattu salausavainten luonnista vastaava luokka Key, viestien käsittelystä vastaava luokka Message sekä käyttäjän kanssa kommunikoinnista vastaava luokka ConsoleIO. Lisäksi yksikkötesteillä on suoritettu yksi integraatiotesti, joka testaa useita metodeja yhdellä testillä. Integraatiotesti luo uuden salausavaimen, salaa viestin sekä purkaa sen käyttäen salausavainta ja varmistaa, että purettu viesti on sama kuin alkuperäinen.