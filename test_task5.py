# -*- coding: utf-8 -*-

import unittest
from task5_vigenere import encrypt, decrypt

class TestUM(unittest.TestCase):
    
    def setUp(self):
        """ Вызывается перед каждым тестом """
        pass

    def tearDown(self):
        """ Вызывается после каждого теста """
        pass
    
    def test_encrypt(self):
        self.assertEqual(encrypt('Привет!','привет'),'юардкд!')
        self.assertEqual(encrypt('Привет, мир! Это секретное сообщение!','секрет'),'ахтткд, энъ! нча вкфакдюуп буатюпэнч!')
        self.assertEqual(encrypt('сова на пне','шерлок'),'йутл ык зтх')
        self.assertEqual(encrypt('1234*&#@','лемон'),'1234*&#@')
        self.assertEqual(encrypt('',''),'')
    
    def test_decrypt(self):
        self.assertEqual(decrypt('юардкд!','привет'),'привет!')
        self.assertEqual(decrypt('ахтткд, энъ! нча вкфакдюуп буатюпэнч!','секрет'),'привет, мир! это секретное сообщение!')
        self.assertEqual(decrypt('йутл ык зтх','шерлок'),'сова на пне')
        self.assertEqual(decrypt('1234*&#@','лемон'),'1234*&#@')
        self.assertEqual(decrypt('',''),'')
       
        

if __name__ == '__main__':
    unittest.main()
