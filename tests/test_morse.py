# coding=utf-8
"""
CERMMorse : test_morse
6/20/2017 : 1:29 PM
Author : James L. Key
"""
import random
from unittest import TestCase

import pymorse

__author__ = 'James L. Key'
__project__ = 'CERMMorse'


class TestMorse(TestCase):
    def setUp(self):
        self.int_morse = pymorse.Morse(version='international')
        self.amer_morse = pymorse.Morse(version='american')
        self.seed = random.seed(None)

    def test_int_morsedecode(self):
        #  create a nice big list to check -- 200 characters
        randtext = random.sample(list(self.int_morse.morse_table), 40)
        randtext = randtext + random.sample(list(self.int_morse.morse_table), 40)
        randtext = randtext + random.sample(list(self.int_morse.morse_table), 40)
        randtext = randtext + random.sample(list(self.int_morse.morse_table), 40)
        randtext = randtext + random.sample(list(self.int_morse.morse_table), 40)
        out = self.int_morse.morseencode(randtext)
        out = self.int_morse.morsedecode(out)
        self.assertEqual(list(out), randtext)

    def test_int_morseencode(self):
        self.maxDiff = None
        #  create a nice big list to check -- 200 characters
        sample = random.sample(list(self.int_morse.rev_morse_table), 40)
        sample = sample + random.sample(list(self.int_morse.rev_morse_table), 40)
        sample = sample + random.sample(list(self.int_morse.rev_morse_table), 40)
        sample = sample + random.sample(list(self.int_morse.rev_morse_table), 40)
        sample = sample + random.sample(list(self.int_morse.rev_morse_table), 40)
        randtext = ''
        for char in sample:
            randtext = randtext + char + '~'
        out = self.int_morse.morsedecode(randtext)
        out = self.int_morse.morseencode(out)
        self.assertEqual(out, randtext)

    def test_amer_morsedecode(self):
        #  create a nice big list to check -- 200 characters
        randtext = random.sample(list(self.amer_morse.morse_table), 40)
        randtext = randtext + random.sample(list(self.amer_morse.morse_table), 40)
        randtext = randtext + random.sample(list(self.amer_morse.morse_table), 40)
        randtext = randtext + random.sample(list(self.amer_morse.morse_table), 40)
        randtext = randtext + random.sample(list(self.amer_morse.morse_table), 40)
        out = self.amer_morse.morseencode(randtext)
        out = self.amer_morse.morsedecode(out)
        self.assertEqual(list(out), randtext)

    def test_amer_morseencode(self):
        self.maxDiff = None
        #  create a nice big list to check -- 200 characters
        sample = random.sample(list(self.amer_morse.rev_morse_table), 40)
        sample = sample + random.sample(list(self.amer_morse.rev_morse_table), 40)
        sample = sample + random.sample(list(self.amer_morse.rev_morse_table), 40)
        sample = sample + random.sample(list(self.amer_morse.rev_morse_table), 40)
        sample = sample + random.sample(list(self.amer_morse.rev_morse_table), 40)
        randtext = ''
        for char in sample:
            randtext = randtext + char + '~'
        out = self.amer_morse.morsedecode(randtext)
        out = self.amer_morse.morseencode(out)
        self.assertEqual(out, randtext)
