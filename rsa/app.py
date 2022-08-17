"""Sovelluksen toteutus"""

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
        self._console_io.write(f"Public key: {pub_key}")
        self._console_io.write(f"Private key: {priv_key}")

    def _encrypt_message(self):
        message = self._console_io.read("Kirjoita salattava viesti: ")
        n_value= int(self._console_io.read("Kirjoita n: "))
        e_value = int(self._console_io.read("Kirjoita e: "))
        encrypted_message = self._messages.encrypt(message, e_value, n_value)
        self._console_io.write(f"Salattu viesti: {encrypted_message}")

    def _decrypt_message(self):
        message = int(self._console_io.read("Kirjoita salattu viesti: "))
        n_value = int(self._console_io.read("Kirjoita n: "))
        d_value = int(self._console_io.read("Kirjoita d: "))
        decrypted_message = self._messages.decrypt(message, d_value, n_value)
        self._console_io.write(f"Purettu viesti: {decrypted_message}")
