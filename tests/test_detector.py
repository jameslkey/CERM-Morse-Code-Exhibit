# coding=utf-8
"""
CERMMorse : test_detector
5/7/2017 : 11:33 PM
Author : James L. Key
"""
from unittest import TestCase

from readconfig import Config
from rpimorsedrv import Detector

__author__ = 'James L. Key'
__project__ = 'CERMMorse'

class TestDetector(TestCase):
    def setUp(self):
        self.config = Config(configpath='../data/config.json')
        self.det = Detector(self.config)

    def test_detect(self):
<<<<<<< HEAD
        self.assertTrue(self.det.detect())
=======
        if os.name != 'posix':
            self.skipTest('Test not supported on non-GPIO device')
        else:
            # warning do not run on non-Raspberry Pi install as it will hang in infinite loop
            self.assertTrue(self.det.detect())
>>>>>>> Fixed code smell in test_detector.py
