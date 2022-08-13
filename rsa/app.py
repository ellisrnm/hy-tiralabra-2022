commands= {
    "0" : "Lopeta",
    "1" : "Luo avaimet",
    "2" : "Salaa viesti"
}

class RsaApp:
    def __init__(self, io, keyprocessing, messageprocessing):
        self._io = io
        self._keys = keyprocessing
        self._messages = messageprocessing

    def run(self):
        self._io.write("RSA-sovellus")
        self._print_instructions()

        while True:
            command = self._io.read("Valitse toiminto: ")

            if not command in commands:
                self._io.write("Virheellinen komento")
                self._print_instructions()
                continue

            if command == "0":
                break

            if command == "1":
                self._generate_keys()

            elif command == "2":
                self._encrypt_message()

    def _print_instructions(self):
        self._io.write("Toiminnot:")
        for command, desc in commands.items():
            self._io.write(f'{command}: {desc}')

    def _generate_keys(self):
        key = self._keys.generate_key()
        self._io.write(key)

    def _encrypt_message(self):
        message = self._io.read("Kirjoita viesti: ")
        encypted_message = self._messages.encrypt(message)
        self._io.write(encypted_message)
