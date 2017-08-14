# -*- coding: utf-8 -*-
"""
Comments go here!!!

:program: CERMMorse
:file: test_morse
:platform: Cross-Platform
:synopsis: Change this text.

.. moduleauthor:: James L. Key <james@bluepenguinslutions.com>

.. py:currentmodule:: Unittests

"""
import random
from unittest import TestCase

import PyMorse

__author__ = 'James L. Key'
__project__ = 'CERMMorse'


class TestMorse(TestCase):
    def setUp(self):
        self.morse = PyMorse.Morse()
        self.seed = random.seed(None)

    def test_morsedecode(self):
        #  create a nice big list to check -- 200 characters
        randtext = random.sample(list(self.morse.morse_table), 40)
        randtext = randtext + random.sample(list(self.morse.morse_table), 40)
        randtext = randtext + random.sample(list(self.morse.morse_table), 40)
        randtext = randtext + random.sample(list(self.morse.morse_table), 40)
        randtext = randtext + random.sample(list(self.morse.morse_table), 40)
        out = self.morse.morseencode(randtext)
        # print(out)
        out = self.morse.morsedecode(out)
        # print(out)
        self.assertEqual(list(out), randtext)

    def test_morseencode(self):
        self.maxDiff = None
        #  create a nice big list to check -- 200 characters
        sample = random.sample(list(self.morse.rev_morse_table), 40)
        sample = sample + random.sample(list(self.morse.rev_morse_table), 40)
        sample = sample + random.sample(list(self.morse.rev_morse_table), 40)
        sample = sample + random.sample(list(self.morse.rev_morse_table), 40)
        sample = sample + random.sample(list(self.morse.rev_morse_table), 40)
        randtext = ''
        for char in sample:
            randtext = randtext + char + "~"
        out = self.morse.morsedecode(randtext)
        # print(out)
        out = self.morse.morseencode(out)
        # print(out)
        self.assertEqual(out, randtext)
