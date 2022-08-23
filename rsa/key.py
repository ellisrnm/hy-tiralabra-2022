"""Salausavainten luominen"""

import random

class Key:
    """
    Sisältää metodit salausavainten luomiseen.
    """

    def __init__(self):
        """
        Luokan konstruktori

        Luo valmiin listan alkuluvuista, jotka ovat pienempiä kuin 5000.
        """
        self.primes_list = self._sieve_of_eratosthenes(5000)

    def _generate_prime_candidate(self, bits: int):
        """
        Palauttaa n-bitin mittaisen suuren satunnaisen luvun. Suuri luku valitaan
        siten, että ensimmäisen bitin tulee olla 1 ja luvun tulee olla pariton.

        Args:
            bits (int): Haluttu bittien lukumäärä n

        Returns:
            Satunnaisluku väliltä 2^(n-1)+1 ja 2^n-1
        """
        candidate = 2
        while candidate % 2 == 0:
            candidate = random.randrange(2**(bits-1)+1, 2**bits-1)
        return candidate

    def _sieve_of_eratosthenes(self, max_value: int):
        """
        Palauttaa listan niistä alkuluvuista, jotka ovat pienempiä tai yhtäsuuria kuin max_value.
        Määrittää alkuluvut käyttäen Eratostheneen seulaa.

        Args:
            max_value (int): Haluttu yläraja, jota pienemmät alkuluvut haetaan

        Returns:
            Palauttaa listan alkulukuja
        """
        primes = [i>1 for i in range(max_value+1)]
        i = 2
        while i*i <= max_value:
            if primes[i] is True:
                for j in range(i**2, max_value+1, i):
                    primes[j] = False
            i += 1
        return [i for i, x in enumerate(primes) if x]

    def _low_level_primality_test(self, prime_candidate: int, max_value: int=5000):
        """
        Nopea alkulukutesti, jossa valittu luku jaetaan muilla alkuluvuilla
        jaollisuuden tarkistamiksi. Jos valittu luku on jaollinen testatuilla
        alkuluvuilla, testi epäonnistuu.

        Args:
            prime_candidate (int): Testattavaksi valittu luku
            max_value (int, optional): Yläraja, jota pienemmillä alkuluvuilla jaollisuus testataan
                                       Oletusarvo 5000

        Returns:
            True, jos luku ei ole jaollinen testatuilla alkuluvuilla
            False, jos luku on jaollinen testatuilla alkuluvuilla
        """
        if max_value == 5000:
            primes_list = self.primes_list
        else:
            primes_list = self._sieve_of_eratosthenes(max_value)
        for div in primes_list:
            if prime_candidate % div == 0 and div**2 <= prime_candidate:
                return False
        return True

    def _miller_rabin_round(self, prime_candidate: int, even_comp: int, divs: int):
        """
        Määrittää Mille-Rabin-algoritmin mukaisen yhden kierroksen avulla, onko tietty
        luku todennäköisesti alkuluku. Testattavaksi valittu luku annetaan muodossa
        prime_candidate = 2^divs*even_comp+1

        Args:
            prime_candidate (int): Testattavaksi valittu luku
            even_comp (int): Testavaksi valitun luvun osa muodossa 2^divs*even_comp+1
            divs (int): Testavaksi valitun luvun osa muodossa 2^divs*even_comp+1

        Returns:
            True, jos n on todennäköisesti alkuluku
            False, jos n on yhdistelmäluku (ei alkuluku)
        """
        rand_val = random.randrange(2, prime_candidate-2)
        result = pow(rand_val, even_comp, prime_candidate)
        if result in (1, prime_candidate-1):
            return True
        for _ in range(divs):
            result = pow(result, 2, prime_candidate)
            if result == prime_candidate-1:
                return True
            if result == 1:
                return False
        return False

    def _miller_rabin_primality_test(self, prime_candidate: int, rounds: int=50):
        """
        Määrittää Mille-Rabin-algoritmin mukaan onko tietty luku todennäköisesti alkuluku.
        Testikierroksia voidaan suorittaa useampia.

        Args:
            prime_candidate (int): Testattavaksi valittu luku
            rounds (int, optional): Testikierrosten lukumäärä, oletusarvo 50

        Returns:
            True, jos n on todennäköisesti alkuluku
            False, jos n on yhdistelmäluku (ei alkuluku)
        """
        even_comp = prime_candidate - 1
        divs = 0
        while even_comp % 2 == 0:
            even_comp >>= 1
            divs += 1
        for _ in range(rounds):
            if not self._miller_rabin_round(prime_candidate, even_comp, divs):
                return False
        return True

    def _generate_prime(self, bits):
        """
        Generoi satunnaisia lukuja ja testaa onko luku alkuluku niin kauan, että todennäköinen
        alkuluku löytyy. Palauttaa n-bitin mittaisen satunnaisen (todennäköisen) alkuluvun.

        Args:
            bits (int): Haluttu bittien lukumäärä n

        Returns:
            Todennäköinen alkuluku
        """
        while True:
            prime_candidate = self._generate_prime_candidate(bits)
            if self._low_level_primality_test(prime_candidate):
                if self._miller_rabin_primality_test(prime_candidate):
                    return prime_candidate

    def _generate_primes(self, bits: int=1024, no_primes: int=2):
        """
        Palauttaa listan, jossa on n-bitin mittaisia satunnaisia (todennäköisiä)
        alkulukuja m kappaletta.

        Args:
            bits (int, optional): Haluttu bittien lukumäärä n, oletusarvo 1024
            no_primes (int, optional): Halutun listan pituus m, oletusarvo 2

        Returns:
            Palauttaa listan satunnaisia alkulukuja
        """
        primes = []
        for _ in range(no_primes):
            primes.append(self._generate_prime(bits))
        return primes

    def _get_greatest_common_divisor(self, a_value: int, b_value: int):
        """
        Selvittää lukujen a ja b suurimman yhteisen tekijän käyttäen
        laajennettua Ekleideen algoritmia

        Args:
            a_value, b_value (int): Luvut, joille haetaan suurinta yhteistä tekijää

        Returns:
            Suurimman yhteisen tekijän sekä luvut, jotka toteuttavat yhtälön gcd(a,b)=ax+by
        """
        if a_value == 0:
            return b_value, 0, 1
        gcd, x_value, y_value = self._get_greatest_common_divisor(b_value % a_value, a_value)
        return gcd, y_value - (b_value // a_value) * x_value, x_value

    def _generate_keys(self, pub_exp: int=65537):
        """
        Generoi RSA-avainparin. Palauttaa julkisen ja salaisen avaimen tarvittavat osat.

        Args:
            pub_exp (int, optional): eksponentti e, oletusarvo 65537

        Returns:
            Luvut priv_exp, pub_exp, mod
            Avainpari (priv_exp,mod) on salainen avain
            Avainpari (pub_exp,mod) on julkinen avain
        """
        p_prime, q_prime = self._generate_primes()
        while p_prime == q_prime:
            p_prime, q_prime = self._generate_primes()
        mod = p_prime * q_prime
        phi_mod = (p_prime - 1) * (q_prime - 1)
        gcd, x_value, _ = self._get_greatest_common_divisor(pub_exp, phi_mod)
        if gcd != 1:
            return None
        priv_exp = x_value if x_value > 0 else x_value + phi_mod
        return priv_exp, pub_exp, mod

    def get_new_keys(self):
        """
        Palauttaa uuden salausavainparin.

        Returns:
            Julkisen avaimen muodossa "pub_exp, mod"
            Yksityisen avaimen muodossa (priv_exp, mod)
        """
        priv_exp, pub_exp, mod = self._generate_keys()
        pub_key = f"{pub_exp},{mod}"
        priv_key = (priv_exp,mod)
        return pub_key, priv_key
