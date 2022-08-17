## Testausdokumentti

### Yksikkötestaus

Yksikkötestaukset toteutetaan ohjelmallisesti. Yksikkötestit voidaan suorittaa seuraavalla komennolla:

    pytest rsa

Yksikkötestauksen kattavuuden voi tarkistaa komennolla:

    coverage run --branch -m pytest

Kattavuudesta voi generoida HTML raportin index.html projektin hakemistoon htmlcov komennolla:

    coverage html

Yksikkötestaukset suoritetaan automaattisesti myös jokaisen päähaaran muutoksien julkaisun yhteydessä. Myös yksikkötestien kattavuus lasketaan samassa yhteydessä automaattisesti. Yksikkötestauksen kattavuusraportti löytyy [Codecovista](https://codecov.io/gh/ellisrnm/hy-tiralabra-2022).

Yksikkötesteillä on testattu salausavainten luonnista vastaava luokka Key, viestien käsittelystä vastaava luokka Message sekä käyttäjän kanssa kommunikoinnista vastaava luokka ConsoleIO.