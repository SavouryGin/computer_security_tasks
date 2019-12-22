# -*- coding: utf-8 -*-

import unittest
from task4_check_signatures import scan_folder

class TestUM(unittest.TestCase):
    
    def setUp(self):
        """ Вызывается перед каждым тестом """
        pass

    def tearDown(self):
        """ Вызывается после каждого теста """
        pass
    
    def test_scan_folder(self):
        self.assertEqual(scan_folder(
                ['samples\\images\\1\\2\\text.txt', 'samples\\images\\1\\32f2eb69feef165ecc31f7d5c6bdf6dc.jpg', 'samples\\images\\1\\text.txt', 'samples\\images\\inx960x640.jpg', 'samples\\images\\text.txt', 'samples\\text.txt', 'samples\\text_ru.txt', 'samples\\ПЗ для магистров и бакалавров.docx'],
                [66, 121, 32, 116, 104, 101, 32, 115, 116, 114, 111, 110, 103, 32, 99, 117]), 
                ['samples\\images\\1\\2\\text.txt', 'samples\\images\\1\\text.txt', 'samples\\images\\text.txt', 'samples\\text.txt'])
        self.assertEqual(scan_folder(
                ['samples\\images\\1\\2\\text.txt', 'samples\\images\\1\\32f2eb69feef165ecc31f7d5c6bdf6dc.jpg', 'samples\\images\\1\\text.txt', 'samples\\images\\inx960x640.jpg', 'samples\\images\\text.txt', 'samples\\text.txt', 'samples\\text_ru.txt', 'samples\\ПЗ для магистров и бакалавров.docx'],
                [112, 111, 119, 101, 114, 32, 116, 111, 32, 109, 97, 107, 101, 32, 116, 104]), 
                ['samples\\images\\1\\2\\text.txt', 'samples\\images\\1\\text.txt', 'samples\\images\\text.txt', 'samples\\text.txt'])
        self.assertEqual(scan_folder(
                ['samples\\images\\1\\2\\text.txt', 'samples\\images\\1\\32f2eb69feef165ecc31f7d5c6bdf6dc.jpg', 'samples\\images\\1\\text.txt', 'samples\\images\\inx960x640.jpg', 'samples\\images\\text.txt', 'samples\\text.txt', 'samples\\text_ru.txt', 'samples\\ПЗ для магистров и бакалавров.docx'],
                [208, 191, 208, 181, 209, 128, 208, 178, 209, 139, 209, 133, 32, 208, 179, 209]), 
                ['samples\\text_ru.txt'])
        

if __name__ == '__main__':
    unittest.main()