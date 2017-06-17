# coding=utf-8
"""
CERMMorse : test_morse
6/17/2017 : 11:59 PM
Author : James L. Key
"""
from unittest import TestCase
import pyammorse
import random

__author__ = 'James L. Key'
__project__ = 'CERMMorse'


class TestMorse(TestCase):
    def setUp(self):
        self.morse = pyammorse.Morse()
        self.seed = random.seed(None)

    def test_morsedecode(self):
        #  create a nice big list to check -- 200 characters
        randtext = random.sample(list(self.morse.amMorseTable), 40)
        randtext = randtext + random.sample(list(self.morse.amMorseTable), 40)
        randtext = randtext + random.sample(list(self.morse.amMorseTable), 40)
        randtext = randtext + random.sample(list(self.morse.amMorseTable), 40)
        randtext = randtext + random.sample(list(self.morse.amMorseTable), 40)
        out = self.morse.morseencode(randtext)
        print(out)
        out = self.morse.morsedecode(out)
        print(out)
        self.assertEqual(list(out), randtext)

    def test_morseencode(self):
        self.maxDiff = None
        #  create a nice big list to check -- 200 characters
        sample = random.sample(list(self.morse.revamMorseTable), 40)
        sample = sample + random.sample(list(self.morse.revamMorseTable), 40)
        sample = sample + random.sample(list(self.morse.revamMorseTable), 40)
        sample = sample + random.sample(list(self.morse.revamMorseTable), 40)
        sample = sample + random.sample(list(self.morse.revamMorseTable), 40)
        randtext = ''
        for char in sample:
             randtext = randtext + char + '~'
        out = self.morse.morsedecode(randtext)
        print(out)
        out = self.morse.morseencode(out)
        print(out)
        self.assertEqual(out, randtext)
