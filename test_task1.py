# -*- coding: utf-8 -*-

import unittest
from task1_hide_and_find_messages import (encode_into_bits, decode_from_bits, 
                                          hide_with_end_spaces, find_with_end_spaces)

class TestUM(unittest.TestCase):
    
    def setUp(self):
        """ Вызывается перед каждым тестом """
        pass

    def tearDown(self):
        """ Вызывается после каждого теста """
        pass
    
    def test_encode_into_bits(self):
        self.assertAlmostEqual(encode_into_bits("f"), "01100110")
        self.assertAlmostEqual(encode_into_bits("ы"), "11011001")
        self.assertAlmostEqual(encode_into_bits("hello"), "0110100001100101011011000110110001101111")
        self.assertAlmostEqual(encode_into_bits("привет"), "110100001101001011001001110101111100010111010100")
        self.assertAlmostEqual(encode_into_bits("HELLO"), "0100100001000101010011000100110001001111")
        self.assertAlmostEqual(encode_into_bits("ПРИВЕТ"), "111100001111001011101001111101111110010111110100")
        self.assertAlmostEqual(encode_into_bits("Hello, World!"), "01001000011001010110110001101100011011110010110000100000010101110110111101110010011011000110010000100001")
        self.assertAlmostEqual(encode_into_bits("Привет, мир!"), "111100001101001011001001110101111100010111010100001011000010000011001101110010011101001000100001")
        self.assertAlmostEqual(encode_into_bits("1234567890"), "00110001001100100011001100110100001101010011011000110111001110000011100100110000")
        self.assertAlmostEqual(encode_into_bits("@#$%^&*(){}[]"), "01000000001000110010010000100101010111100010011000101010001010000010100101111011011111010101101101011101")
        self.assertAlmostEqual(encode_into_bits("Привет, Hello, !?.;:"), "1111000011010010110010011101011111000101110101000010110000100000010010000110010101101100011011000110111100101100001000000010000100111111001011100011101100111010")
        self.assertAlmostEqual(encode_into_bits("A я"), "010000010010000011010001")
    
    def test_decode_from_bits(self):
        self.assertAlmostEqual(decode_from_bits("01100110"), "f")
        self.assertAlmostEqual(decode_from_bits("11011001"), "ы")
        self.assertAlmostEqual(decode_from_bits("0110100001100101011011000110110001101111"), "hello")
        self.assertAlmostEqual(decode_from_bits("110100001101001011001001110101111100010111010100"), "привет")
        self.assertAlmostEqual(decode_from_bits("0100100001000101010011000100110001001111"), "HELLO")
        self.assertAlmostEqual(decode_from_bits("111100001111001011101001111101111110010111110100"), "ПРИВЕТ")
        self.assertAlmostEqual(decode_from_bits("01001000011001010110110001101100011011110010110000100000010101110110111101110010011011000110010000100001"), "Hello, World!")
        self.assertAlmostEqual(decode_from_bits("111100001101001011001001110101111100010111010100001011000010000011001101110010011101001000100001"), "Привет, мир!")
        self.assertAlmostEqual(decode_from_bits("00110001001100100011001100110100001101010011011000110111001110000011100100110000"), "1234567890")
        self.assertAlmostEqual(decode_from_bits("01000000001000110010010000100101010111100010011000101010001010000010100101111011011111010101101101011101"), "@#$%^&*(){}[]")
        self.assertAlmostEqual(decode_from_bits("1111000011010010110010011101011111000101110101000010110000100000010010000110010101101100011011000110111100101100001000000010000100111111001011100011101100111010"), "Привет, Hello, !?.;:")
        self.assertAlmostEqual(decode_from_bits("010000010010000011010001"), "A я")
    
    def test_hide_with_end_spaces(self):
        self.assertEqual(hide_with_end_spaces("samples/text.txt", "010000010010000011010001"), None)
        self.assertEqual(hide_with_end_spaces("asdfkjhal", "010000010010000011010001"), 'Unable to open file')
        self.assertEqual(hide_with_end_spaces(12345, "010000010010000011010001"), 'Unable to open file')
    
    def test_find_with_end_spaces(self):
        self.assertEqual(find_with_end_spaces("secret_spaces.txt"),"010000010010000011010001")
        self.assertEqual(find_with_end_spaces("asdfkjhal"), 'Unable to open file')
        self.assertEqual(find_with_end_spaces(12345), 'Unable to open file')                             

if __name__ == '__main__':
    unittest.main()
