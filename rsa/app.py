"""Sovelluksen toteutus"""

import sys

commands= {
    "0" : "Lopeta",
    "1" : "Luo avaimet",
    "2" : "Salaa viesti",
    "3" : "Pura viesti"
}

class RsaApp:
    """
    Luokka vastaa sovelluksen toiminnasta
    """
    def __init__(self, console_io, keyprocessing, messageprocessing):
        self._console_io = console_io
        self._keys = keyprocessing
        self._messages = messageprocessing

    def run(self):
        """
        Käynnistää ohjelman ja vastaa sovelluksen toiminnoista kunnes käyttäjä lopettaa ohjelman
        """
        self._console_io.write("RSA-sovellus")
        self._print_instructions()

        while True:
            command = self._console_io.read("Valitse toiminto: ")

            if not command in commands:
                self._console_io.write("Virheellinen komento")
                self._print_instructions()
                continue

            if command == "0":
                break

            if command == "1":
                self._generate_keys()

            elif command == "2":
                self._encrypt_message()

            elif command == "3":
                self._decrypt_message()

    def _print_instructions(self):
        self._console_io.write("Toiminnot:")
        for command, desc in commands.items():
            self._console_io.write(f'{command}: {desc}')

    def _generate_keys(self):
        pub_key, priv_key = self._keys.get_new_keys()
        self._console_io.write(f"Julkinen avain: {pub_key}")
        self._console_io.write(f"Yksityisen avaimen exponentti: {priv_key[0]}")
        self._console_io.write(f"Yksityisen avaimen modulo: {priv_key[1]}")

    def _encrypt_message(self):
        message = self._console_io.read("Kirjoita salattava viesti: ")
        while len(message) == 0 or len(message) > 256:
            self._console_io.write("Salattavan viestin pituus on oltava 1-256 merkkiä")
            message = self._console_io.read("Kirjoita salattava viesti: ")
        while True:
            try:
                pub_key = self._console_io.read("Kirjoita julkinen avain: ").split(",")
                pub_exp, pub_mod = [int(x) for x in pub_key]
                encrypted_message = self._messages.encrypt(message, pub_exp, pub_mod)
                self._console_io.write(f"Salattu viesti: {encrypted_message}")
                break
            except KeyboardInterrupt:
                sys.exit(0)
            except:
                self._console_io.write("Syöttämäsi avain ei kelpaa, yritä uudestaan")
                self._console_io.write("Huom! Kirjoita julkinen avain muodossa e,n")

    def _decrypt_message(self):
        while True:
            try:
                message = int(self._console_io.read("Kirjoita salattu viesti: "))
                break
            except KeyboardInterrupt:
                sys.exit(0)
            except:
                self._console_io.write("Syöttämäsi viesti ei kelpaa, yritä uudestaan")
        while True:
            try:
                priv_exp = int(self._console_io.read("Kirjoita yksityisen avaimen exponentti: "))
                priv_mod = int(self._console_io.read("Kirjoita yksityisen avaimen modulo: "))
                decrypted_message = self._messages.decrypt(int(message), priv_exp, priv_mod)
                self._console_io.write(f"Purettu viesti: {decrypted_message}")
                break
            except KeyboardInterrupt:
                sys.exit(0)
            except:
                self._console_io.write("Syöttämäsi avain ei kelpaa, yritä uudestaan")
