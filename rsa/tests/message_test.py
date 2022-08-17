# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=protected-access

import unittest
from message import Message


class TestKey(unittest.TestCase):
    def setUp(self):
        self._messages = Message()

    def test_message_to_int(self):
        self.assertEqual(self._messages._message_to_int('@'),64)

    def test_int_to_message(self):
        self.assertEqual(self._messages._int_to_message(77),'M')

    def test_encrypt(self):
        self.assertEqual(self._messages.encrypt('X', 7, 187), 11)

    def test_decrypt(self):
        self.assertEqual(self._messages.decrypt(11, 7, 187), 'X')
