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

Tulossa