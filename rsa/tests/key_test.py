import unittest
from key import Key


class TestKey(unittest.TestCase):
    def setUp(self):
        self._keys = Key()

    def test_generate_key(self):
        encrypted_key = self._keys.generate_key()
        self.assertEqual(encrypted_key, 'ABC')