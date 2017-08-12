# coding=utf-8
"""
CERMMorse : test_config
5/7/2017 : 11:32 PM
Author : James L. Key
"""
from unittest import TestCase
<<<<<<< HEAD

from readconfig import Config

__author__ = 'James L. Key'
__project__ = 'CERMMorse'
=======
import os
from MorseAppData import MorseAppData
>>>>>>> Refactored readconfig and trainorder(workorder)into MorseAppData package. Still need polishing but functional.


class TestConfig(TestCase):
    def setUp(self):
<<<<<<< HEAD
        self.conf = Config(configpath='../data/config.json')
=======
        loc_path = os.path.dirname(__file__)
        config_file = os.path.join(os.path.sep, loc_path, '..', 'data', 'config.json')
        config_file = os.path.normpath(config_file)
        self.conf = MorseAppData(configpath=config_file)
>>>>>>> Refactored readconfig and trainorder(workorder)into MorseAppData package. Still need polishing but functional.
        self.conf.getconfig()

    def evalcolor(self):
        color = self.conf.Color
        r = color[0]
        g = color[1]
        b = color[2]
        if (r not in range(0, 2)) | (g not in range(0, 2)) | (b not in range(0, 2)):
            return False
        else:
            return True

    def test_getconfig(self):

        self.assertIsInstance(self.conf.LCDPin1, int, 'Config LCDPin1 is not an Integer!!')
        self.assertIn(self.conf.LCDPin1, range(0, 4), 'Config LCDPin1 is not in I2C Range!!')
        self.assertIsInstance(self.conf.LCDPin2, int, 'Config LCDPin2 is not an Integer!!')
        self.assertIn(self.conf.LCDPin2, range(0, 4), 'Config LCDPin1 is not in I2C Range!!')
        self.assertIsInstance(self.conf.RelayPin, int, 'Config RelayPin is not an Integer!!')
        self.assertIn(self.conf.RelayPin, range(0, 27), 'Config LCDPin1 is not in GPIO Range!!')
        self.assertIsInstance(self.conf.MotionDetPin, int, 'Config MotionDetPin is not an Integer!!')
        self.assertIn(self.conf.MotionDetPin, range(0, 27), 'Config LCDPin1 is not in GPIO Range!!')
        self.assertIsInstance(self.conf.WPM, int, 'Config WPM is not an Integer!!')
        self.assertGreaterEqual(self.conf.WPM, 1, 'Config WPM is not Greater than 1!!')
        self.assertIsInstance(self.conf.MaxWPM, int, 'Config MaxWPM is not an Integer!!')
        self.assertGreaterEqual(self.conf.MaxWPM, self.conf.WPM, 'Config MaxWPM is not Greater or Equal to WPM!!')
        self.assertLess(self.conf.MaxWPM, 31, 'Config MaxWPM is Greater than 30WPM -- Seriously? !!')
        self.assertIsInstance(self.conf.SpeedAdjust, bool, 'Config SpeedAdjust is not Boolean!!')
        self.assertIsInstance(self.conf._Colorstr, str, 'Config Stored Color String is not a String!!')
        self.assertTrue(self.evalcolor(),
                        'Parsed Color is not valid - value of number is not (0 or 1) and in form (#, #, #)')
        self.assertIsInstance(self.conf.ParagraphSep, str, 'Config ParagraphSep is not a String!!')
