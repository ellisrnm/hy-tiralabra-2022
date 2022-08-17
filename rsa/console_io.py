"""Kommunikointirajapinta käyttäjälle"""

class ConsoleIO:
    """
    Luokka hoitaa kommunikoinnin käyttäjän ja ohjelman välillä
    """
    def write(self, message: str):
        """
        Kirjoittaa viestin käyttäjän komentoriville

        Args:
            Käyttäjälle näytettävä viesti
        """
        print(message)

    def read(self, prompt: str):
        """
        Pyytää käyttäjältä syötettä

        Args:
            Käyttäjälle näytettävä viesti, joka pyytää käyttäjältä syötettä
        """
        return input(prompt)
