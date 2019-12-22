# -*- coding: utf-8 -*-

import unittest
from task2_hide_and_find_texts import (encode_into_bits, decode_from_bits,
                                       hide_with_double_spaces, find_with_double_spaces)

class TestUM(unittest.TestCase):
    
    def setUp(self):
        """ Вызывается перед каждым тестом """
        pass

    def tearDown(self):
        """ Вызывается после каждого теста """
        pass
    
    def test_encode_into_bits(self):
        self.assertAlmostEqual(encode_into_bits("Привет, Hello, !?.;:"), "1111000011010010110010011101011111000101110101000010110000100000010010000110010101101100011011000110111100101100001000000010000100111111001011100011101100111010")
        self.assertAlmostEqual(encode_into_bits("A я"), "010000010010000011010001")
        
    def test_decode_from_bits(self):
        self.assertAlmostEqual(decode_from_bits("1111000011010010110010011101011111000101110101000010110000100000010010000110010101101100011011000110111100101100001000000010000100111111001011100011101100111010"), "Привет, Hello, !?.;:")
        self.assertAlmostEqual(decode_from_bits("010000010010000011010001"), "A я")
    
    def test_hide_with_double_spaces(self):
        self.assertEqual(hide_with_double_spaces("samples/text.txt", "010000010010000011010001"), None)
        self.assertEqual(hide_with_double_spaces("asdfkjhal", "010000010010000011010001"), 'Unable to open file')
        self.assertEqual(hide_with_double_spaces(12345, "010000010010000011010001"), 'Unable to open file')
    
    def test_find_with_double_spaces(self):
        self.assertEqual(find_with_double_spaces("secret_double.txt"), "010000010010000011010001")
        self.assertEqual(find_with_double_spaces("akdfjhas"), 'Unable to open file')
        self.assertEqual(find_with_double_spaces(12341), 'Unable to open file')
        

if __name__ == '__main__':
    unittest.main()

