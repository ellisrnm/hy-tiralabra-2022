"""Viestien käsittely"""

import math

class Message:
    """
    Sisältää metodit viestien käsittelyyn eli viestin salaamiseen ja salauksen purkamiseen.
    """
    def __init__(self):
        """
        Luokan konstruktori
        """

    def message_to_int(self, msg):
        return int.from_bytes(msg.encode('iso8859-1'), byteorder='little')

    def int_to_message(self, num):
        length = math.ceil(num.bit_length() / 8)
        return num.to_bytes(length, byteorder='little').decode('iso8859-1')

    def encrypt(self, msg, exp, mod):
        base = self.message_to_int(msg)
        return pow(base, exp, mod)

    def decrypt(self, ciphertxt, exp, mod):
        decrypted_int = pow(ciphertxt, exp, mod)
        return self.int_to_message(decrypted_int)
