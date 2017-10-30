# -*- coding: utf-8 -*-

import pdb
import os
import sys
from ..filestream import filestream
import unittest

class FileStreamUnittest(unittest.TestCase):
    def setUp(self):
        self.path = os.path.dirname(os.path.abspath(__file__))

    def test_1(self):
        filename = self.path + "/test1.txt"
        stream = filestream(filename)
        result = stream.get_words()

        self.assertEqual(len(result), 2)
        self.assertEqual(result[0], "test")
        self.assertEqual(result[1], "abc")

    def test_2(self):
        filename = self.path + "/test2.txt"
        stream = filestream(filename)
        result = stream.get_words()
        self.assertEqual(len(result), 13)
        self.assertEqual(result[0], "the")
        self.assertEqual(result[1], "one")
        self.assertEqual(result[2], "where")
        self.assertEqual(result[3], "monica")
        self.assertEqual(result[4], "gets")
        self.assertEqual(result[5], "a")
        self.assertEqual(result[6], "new")
        self.assertEqual(result[7], "roommate")
        self.assertEqual(result[8], "the")
        self.assertEqual(result[9], "pilot")
        self.assertEqual(result[10], "the")
        self.assertEqual(result[11], "uncut")
        self.assertEqual(result[12], "version")



    def test_3(self):
        filename = self.path + "/test3.txt"
        stream = filestream(filename)
        result = stream.get_words()
        self.assertEqual(len(result), 10)
        self.assertEqual(result[0], "scene")
        self.assertEqual(result[1], "central")
        self.assertEqual(result[2], "perk")
        self.assertEqual(result[3], "chandler")
        self.assertEqual(result[4], "joey")
        self.assertEqual(result[5], "phoebe")
        self.assertEqual(result[6], "and")
        self.assertEqual(result[7], "monica")
        self.assertEqual(result[8], "are")
        self.assertEqual(result[9], "there")


    def test_4(self):
        filename = self.path + "/test4.txt"
        stream = filestream(filename)
        result = stream.get_words()
        self.assertEqual(len(result), 14)
        self.assertEqual(result[0], "monica")
        self.assertEqual(result[1], "there")
        self.assertEqual(result[2], "s")
        self.assertEqual(result[3], "nothing")
        self.assertEqual(result[4], "to")
        self.assertEqual(result[5], "tell")
        self.assertEqual(result[6], "he")
        self.assertEqual(result[7], "s")
        self.assertEqual(result[8], "just")
        self.assertEqual(result[9], "some")
        self.assertEqual(result[10], "guy")
        self.assertEqual(result[11], "i")
        self.assertEqual(result[12], "work")
        self.assertEqual(result[13], "with")

    def test_4_strip(self):
        filename = self.path + "/test4.txt"
        stream = filestream(filename)
        result = stream.get_words(True)
        self.assertEqual(len(result), 11)
        self.assertEqual(result[0], "monica")
        self.assertEqual(result[1], "there")
        self.assertEqual(result[2], "nothing")
        self.assertEqual(result[3], "to")
        self.assertEqual(result[4], "tell")
        self.assertEqual(result[5], "he")
        self.assertEqual(result[6], "just")
        self.assertEqual(result[7], "some")
        self.assertEqual(result[8], "guy")
        self.assertEqual(result[9], "work")
        self.assertEqual(result[10], "with")

    def test_5(self):
        filename = self.path + "/test5.txt"
        stream = filestream(filename)
        result = stream.get_words()
        self.assertEqual(len(result), 9)
        self.assertEqual(result[0], "monica")
        self.assertEqual(result[1], "pointing")
        self.assertEqual(result[2], "at")
        self.assertEqual(result[3], "rachel")
        self.assertEqual(result[4], "de")
        self.assertEqual(result[5], "caff")
        self.assertEqual(result[6], "to")
        self.assertEqual(result[7], "all")
        self.assertEqual(result[8], "okay")

    def test_6(self):
        filename = self.path + "/test6.txt"
        stream = filestream(filename)
        result = stream.get_words(True)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], "test")

if __name__ == '__main__':
    unittest.main()