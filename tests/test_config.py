# -*- coding: utf-8 -*-
"""
Comments go here!!!

:program: CERMMorse
:file: test_config
:platform: Cross-Platform
:synopsis: Change this text.

.. moduleauthor:: James L. Key <james@bluepenguinslutions.com>

.. py:currentmodule:: Unittests

"""
from unittest import TestCase
import os
from MorseAppData import MorseAppData


class TestConfig(TestCase):
    def setUp(self):
        loc_path = os.path.dirname(__file__)
        config_file = os.path.join(os.path.sep, loc_path, '..', 'data', 'config.json')
        config_file = os.path.normpath(config_file)
        self.conf = MorseAppData(configpath=config_file)
        self.conf.getconfig()

    def evalcolor(self):
        color = self.conf.color
        r = color[0]
        g = color[1]
        b = color[2]
        if (r not in range(0, 2)) | (g not in range(0, 2)) | (b not in range(0, 2)):
            return False
        else:
            return True

    def test_getconfig(self):

        self.assertIsInstance(self.conf.lcd_pin1, int, 'MorseConfig lcd_pin1 is not an Integer!!')
        self.assertIn(self.conf.lcd_pin1, range(0, 4), 'MorseConfig lcd_pin1 is not in I2C Range!!')
        self.assertIsInstance(self.conf.lcd_pin2, int, 'MorseConfig lcd_pin2 is not an Integer!!')
        self.assertIn(self.conf.lcd_pin2, range(0, 4), 'MorseConfig lcd_pin1 is not in I2C Range!!')
        self.assertIsInstance(self.conf.relay_pin, int, 'MorseConfig relay_pin is not an Integer!!')
        self.assertIn(self.conf.relay_pin, range(0, 27), 'MorseConfig lcd_pin1 is not in GPIO Range!!')
        self.assertIsInstance(self.conf.motion_det_pin, int, 'MorseConfig motion_det_pin is not an Integer!!')
        self.assertIn(self.conf.motion_det_pin, range(0, 27), 'MorseConfig lcd_pin1 is not in GPIO Range!!')
        self.assertIsInstance(self.conf.wpm, int, 'MorseConfig wpm is not an Integer!!')
        self.assertGreaterEqual(self.conf.wpm, 1, 'MorseConfig wpm is not Greater than 1!!')
        self.assertIsInstance(self.conf.max_wpm, int, 'MorseConfig max_wpm is not an Integer!!')
        self.assertGreaterEqual(self.conf.max_wpm, self.conf.wpm, 'MorseConfig max_wpm is not Greater or Equal to wpm!!')
        self.assertLess(self.conf.max_wpm, 31, 'MorseConfig max_wpm is Greater than 30WPM -- Seriously? !!')
        self.assertIsInstance(self.conf.speed_adjust, bool, 'MorseConfig speed_adjust is not Boolean!!')
        self.assertIsInstance(self.conf._color_str, str, 'MorseConfig Stored color String is not a String!!')
        self.assertTrue(self.evalcolor(),
                        'Parsed color is not valid - value of number is not (0 or 1) and in form (#, #, #)')
        self.assertIsInstance(self.conf.paragraph_sep, str, 'MorseConfig paragraph_sep is not a String!!')
