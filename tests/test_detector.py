# -*- coding: utf-8 -*-
"""
Comments go here!!!

:program: CERMMorse
:file: test_detector
:platform: Cross-Platform
:synopsis: Change this text.

.. moduleauthor:: James L. Key <james@bluepenguinslutions.com>

.. py:currentmodule:: Unittests

"""
import os
from unittest import TestCase
from MorseAppData import MorseAppData
from RPiMorseDrv import Detector


class TestDetector(TestCase):
    def setUp(self):
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
        if os.name != 'posix':
            self.skipTest('Test not supported on non-GPIO device')
        else:
            # warning do not run on non-Raspberry Pi install as it will hang in infinite loop
            self.assertTrue(self.det.detect())
