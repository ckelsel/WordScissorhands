# -*- coding: utf-8 -*-

import os
import sys
from ..filestream import filestream
import unittest

class FileStreamUnittest(unittest.TestCase):
    def setUp(self):
        self.path = os.path.dirname(os.path.abspath(__file__))

    def test_get_words(self):
        filename = self.path + "/test1.txt"
        stream = filestream(filename)
        result = stream.get_words()

        self.assertEqual(len(result), 2)
        self.assertEqual(result[0], "test")
        self.assertEqual(result[1], "abc")


if __name__ == '__main__':
    unittest.main()