# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=protected-access

import unittest
from key import Key
from message import Message


class TestIntegration(unittest.TestCase):
    def setUp(self):
        self._keys = Key()
        self._messages = Message()

    def test_keygen_encrypt_decrypt(self):
        pub_key, priv_key = self._keys.get_new_keys()
        pub_exp, pub_mod = [int(x) for x in pub_key.split(",")]
        priv_exp, priv_mod = priv_key
        message = """Lorem ipsum dolor sit amet, consectetur adipiscing elit."""
        encrypted_message = self._messages.encrypt(message, pub_exp, pub_mod)
        decrypted_message = self._messages.decrypt(encrypted_message, priv_exp, priv_mod)
        self.assertEqual(message, decrypted_message)
