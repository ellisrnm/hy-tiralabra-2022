## Käyttöohje

Sovellus on toteutettu yksinkertaisena Python-komentorivisovelluksena. Sinulla tulee olla Python asennettuna koneellesi, jotta voit asentaa sovelluksen.

### Asennus

Kloonaa projekti ensin omalle koneellesi haluamaasi hakemistoon.

Luo sovellukselle uusi virtuaaliympäristö. Mene hakemistoon, johon haluat luoda uuden ympäristön, tai vaihtoehtoisesti kirjoita koko polku _rsaproj_-kohdan tilalle. Voit halutessasi nimetä virtuaaliympäristön myös muulla nimellä kuin _rsaproj_. Suorita komento:

    python3 -m venv rsaproj

Aktivoi juuri luomasi virtuaaliympäristö komennolla:

    source rsaproj/bin/activate

Huomioi, että sinun tulee olla samassa hakemistossa mihin loit virtuaaliympäristön aikaisemmin. Muussa tapauksessa kirjoita _rsaproj_ tilalle hakemiston koko polku.

Seuraavaksi asenna projektin riippuvuudet virtuaaliympäristössä käyttämällä seuraavaa komentoa. Sinun tulee olla projektin hakemistossa.

    pip3 install -r requirements.txt

### Käynnistys

Käynnistä ohjelma käyttämällä seuraavaa komentoa:

    python3 rsa

### Ohjelman toiminnallisuudet

Ohjelmalla on kolme erilaista toimintoa: salausavaimien luominen, viestin salaaminen sekä salatun viestin purkaminen. Toiminto valitaan komentorivillä antamalla sovellukselle syötteenä komentoa vastaava luku ohjeistuksen mukaan.

Valitsemalla salausavaimien luomisen ohjelma generoi uuden salausavainparin ja palauttaa syötteenä sekä yksityisen avaimen että julkisen avaimen osat. Nämä käyttäjän tulisi ottaa talteen.

Valitsemalla viestin salaamisen käyttäjän tulee antaa ensin syötteenä se viesti, jonka käyttäjä haluaa salata. Viesti saa olla maksimissaan 256 merkkiä. Sen jälkeen käyttäjän tulee syöttää ohjelmalle viestin vastaanottajan julkisen avaimen osat e ja n. Julkisen avaimen osat tulee syöttää molemmat yhdellä kerralla muodossa e,n. Ohjelma tulostaa komentoriville salatun viestin.

Valitsemalla viestin purkamisen käyttäjän tulee antaa syötteenä se viesti, joka on salattu käyttäen vastaanottajan julkista avainta. Sen jälkeen käyttäjän tulee syöttää ohjelmalle viestin vastaanottajan yksityisen avaimen osat d ja n. Yksityisen avaimen osat syötetään yksi kerrallaan, ensin ohjelma pyytää yksityisen avaimen eksponenttia d ja sen jälkeen moduloa n. Jos syötetty avain on ollut oikea, ohjelma tulostaa komentoriville puretun viestin.