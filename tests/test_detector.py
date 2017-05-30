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
        self.assertTrue(self.det.detect())
