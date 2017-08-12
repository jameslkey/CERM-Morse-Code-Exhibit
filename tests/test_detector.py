# coding=utf-8
"""
CERMMorse : test_detector
5/7/2017 : 11:33 PM
Author : James L. Key
"""
from unittest import TestCase
<<<<<<< HEAD
<<<<<<< HEAD
=======
from MorseAppData import MorseConfig
=======
from MorseAppData import MorseAppData
>>>>>>> Minor logic change to trainorder and fixed tests.
from RPiMorseDrv import Detector
>>>>>>> Refactored readconfig and trainorder(workorder)into MorseAppData package. Still need polishing but functional.

from readconfig import Config
from rpimorsedrv import Detector

__author__ = 'James L. Key'
__project__ = 'CERMMorse'

class TestDetector(TestCase):
    def setUp(self):
<<<<<<< HEAD
        self.config = Config(configpath='../data/config.json')
        self.det = Detector(self.config)

    def test_detect(self):
<<<<<<< HEAD
        self.assertTrue(self.det.detect())
=======
=======
        self._config_path = os.path.dirname(__file__)
        self._config_path = os.path.join(os.path.sep, self._config_path, '..', 'data', 'config.json')
        self.config = MorseAppData(configpath=self._config_path)
        self.config.getconfig()
        self.pin = self.config.motion_det_pin
        self.det = Detector(self.pin)

    def test_detect(self):
        """
        .. todo:: Write unittest.mock object
        :return:
        """
>>>>>>> Refactored readconfig and trainorder(workorder)into MorseAppData package. Still need polishing but functional.
        if os.name != 'posix':
            self.skipTest('Test not supported on non-GPIO device')
        else:
            # warning do not run on non-Raspberry Pi install as it will hang in infinite loop
            self.assertTrue(self.det.detect())
>>>>>>> Fixed code smell in test_detector.py
