# -*- coding: utf-8 -*-

import unittest
from task3_hide_and_find_translit_text import (encode_into_bits, decode_from_bits,
                                       hide_with_translit, find_with_translit)

class TestUM(unittest.TestCase):
    
    def setUp(self):
        """ Вызывается перед каждым тестом """
        pass

    def tearDown(self):
        """ Вызывается после каждого теста """
        pass
    
    def test_encode_into_bits(self):
        self.assertAlmostEqual(encode_into_bits("A я"), "010000010010000011010001")
        
    def test_decode_from_bits(self):
        self.assertAlmostEqual(decode_from_bits("010000010010000011010001"), "A я")
    
    def test_hide_with_translit(self):
        self.assertEqual(hide_with_translit("samples/text_ru.txt", "010000010010000011010001"), None)
        self.assertEqual(hide_with_translit("asdfkjhal", "010000010010000011010001"), 'Unable to open file')
        self.assertEqual(hide_with_translit(12345, "010000010010000011010001"), 'Unable to open file')
    
    def test_find_with_translit(self):
        self.assertEqual(find_with_translit("secret_translit.txt"), "010000010010000011010001")
        self.assertEqual(find_with_translit("akdfjhas"), 'Unable to open file')
        self.assertEqual(find_with_translit(12341), 'Unable to open file')
        

if __name__ == '__main__':
    unittest.main()