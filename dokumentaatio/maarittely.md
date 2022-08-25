## Määrittelydokumentti

Aihe: RSA-salaus

Käytettävä ohjelmointikieli: Python (Huom! Myös vertaisarviointi ainoastaan Python)

Opinto-ohjelma: Tietojenkäsittelytieteen kandidaatti (TKT)

Projektin kieli: dokumentaation ja ohjelman toimintojen kielenä suomi, koodin kielenä englanti

### Aiheen kuvaus

Ohjelman tarkoituksena on salata ja purkaa lyhyitä viestejä RSA-salauksella itse generoiduilla avaimilla. RSA on epäsymmetrinen salausalgoritmi, joka käyttää viestien salaamiseen vastaanottajan julkista avainta (lähettäjän tiedossa, mahdollisesti julkisesti jaettu) ja salauksen purkamiseen vastaanottajan yksityistä avainta (salainen, ainoastaan vastaanottajan tiedossa). Vastaanottajan julkisella avaimella salatun viestin salaus voidaan purkaa ainoastaan vastaanottajan yksityisellä avaimella.

![RSA-salaus](kuvat/rsa.png?raw=true)

Ylläolevassa kuvassa on havainnoillistettu RSA-salauksen toimintaa. Tässä ohjelmassa on toteutettu uusien 2048-bittisten salausavainten luonti sekä 1-256 merkin pituisen viestin salaaminen ja purkaminen käyttäen ohjelmalla luotuja avaimia.

### Työssä käytettäviä yleisiä algoritmeja

- Alkulukujen valitseminen salausavainten luomista varten:
    - Eratostheneen seula alkulukujen etsimiseen äärellisestä lukujoukosta
    - Miller-Rabin -algoritmi isojen alkulukujen tunnistamiseen
- Salausavaimen laskeminen:
    - Laajennettu Ekleideen algoritmi yksityisen avaimen eksponentin laskemiseksi
