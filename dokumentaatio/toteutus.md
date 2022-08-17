## Toteutusdokumentti

### Ohjelman yleisrakenne

Avainten luonnista vastaa luokka Key ja viestin käsittelystä vastaa luokka Message.

### Avainten luonti

_Sovelluksen avainten luonnin kuvaus keskeneräinen_

### Viestin salaaminen ja salauksen purkaminen

Salattu viesti c voidaan laskea seuraavan kaavan mukaan:

$c = m^e (mod N)$

Kaavassa m on alkuperäinen viesti, jonka esitysmuoto on muutettu kokonaisluvuksi. Arvot e ja N tulevat viestin vastaanottajan julkisesta avaimesta. Ohjelma kysyy näitä arvoja syötteenä ennen salatun viestin laskemista.

Salattu viesti m voidaan palauttaa c:n arvosta seuraavan kaavan mukaan:

$m = c^d (mod N)$

Kaavassa c on viesti, joka on salattu käyttäen vastaanottajan julkista avainta. Arvot d ja N tulevat viestin vastaanottajan yksityisestä avaimesta. Ohjelma kysyy näitä arvoja syötteenä ennen salatun viestin purkamista. Sen jälkeen m muutetaan vielä kokonaisluvun esitysmuodosta takaisin tekstiksi.

### Lähteet

- [RSA](https://fi.wikipedia.org/wiki/RSA) Wikipedia. Viitattu 17.8.2022.



