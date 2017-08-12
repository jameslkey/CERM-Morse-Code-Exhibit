# coding=utf-8
"""
CERMMorse : test_relay
5/7/2017 : 11:32 PM
Author : James L. Key
"""
import os
from unittest import TestCase
<<<<<<< HEAD

from readconfig import Config
from rpimorsedrv import Relay

__author__ = 'James L. Key'
__project__ = 'CERMMorse'
=======
from MorseAppData import MorseAppData
from RPiMorseDrv import Relay
import os
>>>>>>> Minor logic change to trainorder and fixed tests.


class TestRelay(TestCase):
    def setUp(self):
<<<<<<< HEAD
        p = os.path.dirname(os.getcwd())
        p = os.path.join(p, 'CERMMorse')
        p = os.path.join(p, 'data')
        p = os.path.join(p, 'config.json')
        os.path.normpath(p)
        self.config = Config(configpath=p)
        self.config.getconfig()
        self.relay = Relay(self.config)
=======
        loc_path = os.path.dirname(__file__)
        config_file = os.path.join(os.path.sep, loc_path, '..', 'data', 'config.json')
        config_file = os.path.normpath(config_file)
        self.conf = MorseAppData(configpath=config_file)
        self.conf.getconfig()
        self.relay = Relay(pin=self.conf.relay_pin, invert=True)
>>>>>>> Minor logic change to trainorder and fixed tests.

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
