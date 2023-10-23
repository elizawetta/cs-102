import unittest

"""Testing tasks lab2"""
import unittest
from src.lab2.caesar import encrypt_caesar, decrypt_caesar


class CalculatorTestCase(unittest.TestCase):
    def test_encrypt_default_shift(self):
        self.assertEqual(encrypt_caesar('PYTHON'), 'SBWKRQ')

    def test_encrypt_zero_shift(self):
        self.assertEqual(encrypt_caesar('Caesar', 0), 'Caesar')

    def test_encrypt_empty_text(self):
        self.assertEqual(encrypt_caesar('', 10), '')

    def test_encrypt_big_shift(self):
        self.assertEqual(encrypt_caesar('Caesar shifr the best', 378), 'Qosgof gvwtf hvs psgh')

    def test_encrypt_negative_shift(self):
        self.assertEqual(encrypt_caesar('Caesar shifr the best', -1), 'Bzdrzq rgheq sgd adrs')

    def test_decrypt_default_shift(self):
        self.assertEqual(decrypt_caesar('SBWKRQ'), 'PYTHON')

    def test_decrypt_zero_shift(self):
        self.assertEqual(decrypt_caesar('Caesar', 0), 'Caesar')

    def test_decrypt_empty_text(self):
        self.assertEqual(decrypt_caesar('', 10), '')

    def test_decrypt_big_shift(self):
        self.assertEqual(decrypt_caesar('Qosgof gvwtf hvs psgh', 378), 'Caesar shifr the best')

    def test_decrypt_negative_shift(self):
        self.assertEqual(decrypt_caesar('Bzdrzq rgheq sgd adrs', -1), 'Caesar shifr the best')





if __name__ == '__main__':
    unittest.main()
