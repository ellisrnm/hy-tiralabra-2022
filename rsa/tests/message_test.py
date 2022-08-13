import unittest
from message import Message


class TestKey(unittest.TestCase):
    def setUp(self):
        self._messages = Message()

    def test_encypt(self):
        message = 'Hei!'
        encrypted_message = self._messages.encrypt(message)
        self.assertEqual(encrypted_message, 'slkdflskd')
