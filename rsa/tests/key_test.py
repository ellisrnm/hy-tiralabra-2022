# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=protected-access

import unittest
import random
from mock import patch
from key import Key


class TestKey(unittest.TestCase):
    primes_for_testing = [
        503212972075790077689843183272089578073978341777935623962802314798486803226877025013207038565508283675397899998287987517653881742649820179733221712819,
        996595909191577319011942214653721673099706111368127186597531780621318625075760935946188480992672681319019711691848070090224860630793789738004510232137,
        615673454856424837270661179333262276853972036391430563660069086976425477112065486558265760512227658843660638661148967417813159387819577610260021861801,
        155332862755868938796953900725775502334311649456869960170714087425808561448596477446192956709439596199610632233700339190632215991875778077927452842831,
        179675968174475417118941289755488190302504103960531884769958325425402420908809217170247374656874897884558401581809563263689655752854968696257874007233,
        890283996493453210438453353170827303735551182393965831719200020476023169533678320911802669321804008154795944975028603109353119392295675016411866355249,
        584380824864610305240963635694938481501515092177875836390598707076756937986312147020666385696692559456319523849659571093542779939434720367861940975223,
        319174708045063982879226580426779980195214699546752996936758137019785786520145372626592466043617673596050188380146226088504664759536444451138236121683,
        653162192066100869795726507921175022009056499719597071059145075800370795695996453269213192410678928828132277810333359199552461142842304408568409807419,
        107960670721583756638226283815083658420412450227408281620196245569525837361603283189872567287466076386118603969031509451890921960642180724398023575327
    ]

    def setUp(self):
        self._keys = Key()
        self._bits = 1024

    def test_prime_candidate(self):
        value = self._keys._generate_prime_candidate(self._bits)
        self.assertEqual(value % 2, 1)
        self.assertEqual(value.bit_length(), self._bits)
        self.assertTrue(2**(self._bits-1)+1 <= value <= 2**self._bits-1)

    def test_sieve_of_eratosthenes(self):
        self.assertEqual(self._keys._sieve_of_eratosthenes(13), [2, 3, 5, 7, 11, 13])
        primes_list = self._keys._sieve_of_eratosthenes(100)
        self.assertEqual(len(primes_list), 25)
        self.assertTrue(max(primes_list)<100)

    def test_low_level_primality(self):
        self.assertTrue(self._keys._low_level_primality_test(97))
        self.assertTrue(self._keys._low_level_primality_test(101, max_value=100))
        self.assertFalse(self._keys._low_level_primality_test(98))

    def test_miller_rabin_primality_test(self):
        self.assertFalse(self._keys._miller_rabin_primality_test(252601))
        self.assertTrue(self._keys._miller_rabin_primality_test(760847))
        self.assertFalse(self._keys._miller_rabin_primality_test(345792881913515564780416674235914339384284726941180726124021923278025499806531620229037290455234119767869017779025288896244405824188411540507837043639097052230607393995657269231631962847488419821745265495843550310544266946174746773874577253755326814285882324216174561250515236062639329030816699625700))
        self.assertTrue(self._keys._miller_rabin_primality_test(553877674025683592866415966275426851645874449815767098394301058341953349482933005353377657008382916473856740466238137069245386552197503785150027164601040874993688927858560210290760076697949830994314889874894651361882347688961052428123527299340483271490976485747791142099395079858334974381502116191987))
        for _ in range(10):
            prime_a = random.choice(self.primes_for_testing)
            prime_b = random.choice(self.primes_for_testing)
            self.assertTrue(self._keys._miller_rabin_primality_test(prime_a))
            self.assertFalse(self._keys._miller_rabin_primality_test(prime_a * prime_b))

    def test_generate_primes(self):
        primes_list = self._keys._generate_primes(no_primes=3)
        self.assertEqual(primes_list[0].bit_length(), self._bits)
        self.assertEqual(len(primes_list), 3)

    def test_get_greatest_common_divisor(self):
        self.assertEqual(self._keys._get_greatest_common_divisor(12,8)[0], 4)
        self.assertEqual(self._keys._get_greatest_common_divisor(1220,516)[0], 4)
        prime_a = random.choice(self.primes_for_testing)
        prime_b = random.choice(self.primes_for_testing)
        composite = random.getrandbits(500)
        self.assertEqual(self._keys._get_greatest_common_divisor(prime_a*composite, prime_b*composite)[0], composite)
        self.assertEqual(self._keys._get_greatest_common_divisor(prime_a, prime_b)[0], 1)

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
