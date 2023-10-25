import unittest

"""Testing Caesar Cipher"""
import unittest
from src.lab2.caesar import encrypt_caesar, decrypt_caesar


class CaesarTestCase(unittest.TestCase):
    def test_encrypt_default_shift(self):
        self.assertEqual(encrypt_caesar('PYTHON'), 'SBWKRQ')

    def test_encrypt_zero_shift(self):
        self.assertEqual(encrypt_caesar('Caesar', 0), 'Caesar')

    def test_encrypt_empty_text(self):
        self.assertEqual(encrypt_caesar('', 10), '')

    def test_encrypt_big_shift(self):
        self.assertEqual(encrypt_caesar('Caesar cipher the best', 378), 'Qosgof qwdvsf hvs psgh')

    def test_encrypt_negative_shift(self):
        self.assertEqual(encrypt_caesar('Caesar cipher the best', -1), 'Bzdrzq bhogdq sgd adrs')

    def test_decrypt_default_shift(self):
        self.assertEqual(decrypt_caesar('SBWKRQ'), 'PYTHON')

    def test_decrypt_zero_shift(self):
        self.assertEqual(decrypt_caesar('Caesar', 0), 'Caesar')

    def test_decrypt_empty_text(self):
        self.assertEqual(decrypt_caesar('', 10), '')

    def test_decrypt_big_shift(self):
        self.assertEqual(decrypt_caesar('Qosgof qwdvsf hvs psgh', 378), 'Caesar cipher the best')

    def test_decrypt_negative_shift(self):
        self.assertEqual(decrypt_caesar('Bzdrzq bhogdq sgd adrs', -1), 'Caesar cipher the best')


if __name__ == '__main__':
    unittest.main()
