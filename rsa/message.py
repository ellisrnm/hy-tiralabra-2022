"""Viestien käsittely"""

import math

class Message:
    """
    Sisältää metodit viestien käsittelyyn eli viestin salaamiseen ja salauksen purkamiseen
    """
    def __init__(self):
        """
        Luokan konstruktori
        """

    def _message_to_int(self, msg: str):
        """
        Muuttaa viestin esitysmuodon tekstimuotoisesta kokonaisluvuksi

        Args:
            msg: Alkuperäinen viesti tekstimuodossa

        Returns:
            Viesti kokonaislukuna
        """
        return int.from_bytes(msg.encode('iso8859-1'), byteorder='little')

    def _int_to_message(self, num: int):
        """
        Muuttaa viestin esitysmuodon kokonaisluvusta tekstimuotoiseksi

        Args:
            msg: Viesti kokonaislukuna

        Returns:
            Viesti tekstimuodossa
        """
        length = math.ceil(num.bit_length() / 8)
        return num.to_bytes(length, byteorder='little').decode('iso8859-1')

    def encrypt(self, msg: str, exp: int, mod: int):
        """
        Laskee alkuperäisestä viestistä salatun viestin

        Args:
            msg: Alkuperäinen viesti, joka halutaan salata
            exp: Vastaanottajan julkisen salausavaimen eksponenttiosa
            mod: Vastaanottajan julkisen salausavaimen modulo-osa

        Returns:
            Salattu viesti
        """
        base = self._message_to_int(msg)
        return pow(base, exp, mod)

    def decrypt(self, ciphertxt: str, exp: int, mod: int):
        """
        Purkaa salatun viestin

        Args:
            ciphertxt: Purettava viesti, joka on salattu vastaanottajan julkista avainta käyttäen
            exp: Vastaanottajan yksityisen salausavaimen eksponenttiosa
            mod: Vastaanottajan yksityisen salausavaimen modulo-osa

        Returns:
            Purettu viesti
        """
        decrypted_int = pow(ciphertxt, exp, mod)
        return self._int_to_message(decrypted_int)
