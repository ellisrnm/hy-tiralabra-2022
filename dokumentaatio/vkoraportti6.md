## Viikkoraportti 6

### Projektin eteneminen viikolla 6

- Ohjelman toiminnallisuuksien parannuksia esim. virheellisten syötteiden käsittely
- Ohjelman ongelmien korjailu aikaisemman palautteen perusteella
- Dokumentaation kirjoittaminen loppuun

Viikolla 6 projektiin käytetty yhteensä aikaa 9 tuntia. Lisäksi vertaisarvioinnin tekemiseen käytin 3 tuntia.

Tällä viikolla olen tehnyt pieniä korjauksia ohjelmaan vertaispalautteen ja ohjaajan palautteen perusteella. Minulla on näihin liittyen vielä korjailtavaa etenkin oikeellisuustestauksessa. 

Minulla on vielä epäselvyyksiä avaimen pituuden ja salattavan viestin enimmäispituudesta. Salausavaimen pituus on siis modulon bittimäärä? Olin aikaisemmin sekoittanut tämän valitsemani alkuluvun pituuteen. Omassa ohjelmassani olen tehnyt niin, että alkuluvuksi valitaan 1024-bittinen luku jonka ensimmäinen bitti on 1 (eli väliltä 2^(n-1)+1 ja 2^n-1), siten modulon p*q bittimääräksi pitäisi tulla 2048 mutta tämähän ei ole välttämättä aina totta vaan voi olla lyhyempikin? Onko siis salattavan viestin enimmäispituus silti aina 256 merkkiä? Pitäisikö ohjelmassa varmistaa, että modulon bittimäärä on 2048 vai tarkoitetaan 2048-bittisellä avaimella n. 2048-bittistä avainta?

Muita avoimia kysymyksiä on vielä algoritmien aikavaativuuksien selvittäminen.

### Seuraavat tehtävät

- Aikavaativuuksien toteutumisen testaus
- Ohjelman oikeellisuustestauksen parantaminen
- Kurssin demotilaisuus
- Projektin viimeistely
