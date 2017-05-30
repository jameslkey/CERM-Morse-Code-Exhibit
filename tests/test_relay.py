# coding=utf-8
"""
CERMMorse : test_relay
5/7/2017 : 11:32 PM
Author : James L. Key
"""
import os
from unittest import TestCase

from readconfig import Config
from rpimorsedrv import Relay

__author__ = 'James L. Key'
__project__ = 'CERMMorse'


class TestRelay(TestCase):
    def setUp(self):
        p = os.path.dirname(os.getcwd())
        p = os.path.join(p, 'CERMMorse')
        p = os.path.join(p, 'data')
        p = os.path.join(p, 'config.json')
        os.path.normpath(p)
        self.config = Config(configpath=p)
        self.config.getconfig()
        self.relay = Relay(self.config)

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
