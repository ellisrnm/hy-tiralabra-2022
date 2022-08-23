# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=protected-access

import unittest
from mock import patch
from key import Key


class TestKey(unittest.TestCase):
    def setUp(self):
        self._keys = Key()
        self._bits = 1024

    def test_prime_candidate(self):
        value = self._keys._generate_prime_candidate(self._bits)
        self.assertEqual(value % 2, 1)
        self.assertEqual(value.bit_length(), self._bits)
        self.assertTrue(2**(self._bits-1)+1 <= value <= 2**self._bits-1)

    def test_sieve_of_eratosthenes(self):
        primes_list = self._keys._sieve_of_eratosthenes(100)
        self.assertEqual(len(primes_list), 25)
        self.assertTrue(max(primes_list)<100)

    def test_low_level_primality(self):
        self.assertTrue(self._keys._low_level_primality_test(97))
        self.assertTrue(self._keys._low_level_primality_test(101, max_value=100))
        self.assertFalse(self._keys._low_level_primality_test(98))

    def test_miller_rabin_primality_test(self):
        self.assertFalse(self._keys._miller_rabin_primality_test(252601))
        self.assertTrue(self._keys._miller_rabin_primality_test(97))
        self.assertFalse(self._keys._miller_rabin_primality_test(98))

    def test_generate_primes(self):
        primes_list = self._keys._generate_primes(no_primes=3)
        self.assertEqual(primes_list[0].bit_length(), self._bits)
        self.assertEqual(len(primes_list), 3)

    def test_get_greatest_common_divisor(self):
        self.assertEqual(self._keys._get_greatest_common_divisor(12,8)[0], 4)
        self.assertEqual(self._keys._get_greatest_common_divisor(1220,516)[0], 4)

    def test_generate_keys(self):
        with patch.object(Key, '_generate_primes') as mock_method:
            mock_method.return_value = [3, 11]
            result = self._keys._generate_keys(pub_exp=3)
            self.assertEqual((7,3,33), result)

    def test_get_new_keys(self):
        with patch.object(Key, '_generate_keys') as mock_method:
            mock_method.return_value = [1, 2, 3]
            result = self._keys.get_new_keys()
            self.assertEqual("2,3", result[0])
            self.assertEqual((1,3), result[1])
