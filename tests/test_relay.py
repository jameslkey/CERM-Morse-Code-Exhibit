# -*- coding: utf-8 -*-
"""
Comments go here!!!

:program: CERMMorse
:file: test_relay
:platform: Cross-Platform
:synopsis: Change this text.

.. moduleauthor:: James L. Key <james@bluepenguinslutions.com>

.. py:currentmodule:: Unittests

"""
from unittest import TestCase
from unittest import skip
from MorseAppData import MorseAppData
from RPiMorseDrv import Relay
import os


class TestRelay(TestCase):
    def setUp(self):
        loc_path = os.path.dirname(__file__)
        config_file = os.path.join(os.path.sep, loc_path, '..', 'data', 'config.json')
        config_file = os.path.normpath(config_file)
        self.conf = MorseAppData(configpath=config_file)
        self.conf.getconfig()
        self.relay = Relay(pin=self.conf.relay_pin, invert=True)

    def test_fire(self):
        self.relay.fire(1)

    def test_pause(self):
        self.relay.pause(.25)

    def test_both(self):
        self.test_fire()
        self.test_pause()
        self.test_fire()
        self.test_pause()
        self.test_fire()
