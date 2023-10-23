import unittest

"""Testing Vigenre Cipher"""
import unittest
from src.lab2.vigenre import encrypt_vigenere, decrypt_vigenere


class VigenreTestCase(unittest.TestCase):
    def test_encrypt_empty_keyword(self):
        self.assertEqual(encrypt_vigenere('PYTHON', ''), 'ERROR')

    def test_encrypt_short_keyword(self):
        self.assertEqual(encrypt_vigenere('PYTHON', 'A'), 'PYTHON')

    def test_encrypt_long_keyword(self):
        self.assertEqual(encrypt_vigenere('Vigenre_Cipher', 'ololololololololololo'), 'Jtupbcs_Qtdssc')

    def test_decrypt_empty_keyword(self):
        self.assertEqual(decrypt_vigenere('PYTHON', ''), 'ERROR')

    def test_decrypt_short_keyword(self):
        self.assertEqual(decrypt_vigenere('PYTHON', 'A'), 'PYTHON')

    def test_decrypt_long_keyword(self):
        self.assertEqual(decrypt_vigenere('Jtupbcs_Qtdssc', 'ololololololololololo'), 'Vigenre_Cipher')


if __name__ == '__main__':
    unittest.main()
