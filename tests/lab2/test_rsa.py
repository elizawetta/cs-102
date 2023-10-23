import unittest

"""Testing RSA functions"""
import unittest
from src.lab2.rsa import is_prime, gcd, multiplicative_inverse


class RSATestCase(unittest.TestCase):
    def test_1_is_prime(self):
        self.assertEqual(is_prime(1), False)

    def test_0_is_prime(self):
        self.assertEqual(is_prime(0), False)

    def test_negative_is_prime(self):
        self.assertEqual(is_prime(-100), False)

    def test_2_is_prime(self):
        self.assertEqual(is_prime(2), True)

    def test_prime_numbers_1(self):
        self.assertEqual(is_prime(11), True)

    def test_prime_numbers_2(self):
        self.assertEqual(is_prime(211), True)

    def test_not_prime_numbers_1(self):
        self.assertEqual(is_prime(10), False)

    def test_not_prime_numbers_2(self):
        self.assertEqual(is_prime(5555), False)

    def test_gcd_same_numbers(self):
        self.assertEqual(gcd(345, 345), 345)

    def test_gcd_prime_numbers(self):
        self.assertEqual(gcd(2, 13), 1)

    def test_gcd_1(self):
        self.assertEqual(gcd(1, 15), 1)

    def test_gcd_2(self):
        self.assertEqual(gcd(15, 150), 15)

    def test_gcd_3(self):
        self.assertEqual(gcd(15, 49), 1)

    def test_multiplicative_inverse_1(self):
        self.assertEqual(multiplicative_inverse(7, 40), 23)

    def test_multiplicative_inverse_2(self):
        self.assertEqual(multiplicative_inverse(3, 17), 6)


if __name__ == '__main__':
    unittest.main()
