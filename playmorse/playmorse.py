# -*- coding: utf-8 -*-
"""
Comments go here!!!

Parsing Control for Adafruit_CharLCD in CERMMorse.

:program: CERMMorse
:file: playmorse
:platform: Cross-Platform
:synopsis: Change this text.

.. moduleauthor:: James L. Key <james@bluepenguinslutions.com>

.. py:currentmodule:: PlayMorse

"""

from math import floor
from RPiMorseDrv import Relay

__author__ = 'James L. Key'
__project__ = 'CERM20'


class PlayMorse:
    r"""

    """
    def __init__(self, wpm: int, relaypin: int, invertrelay: bool = False):
        r"""

        :param wpm:
        :param relaypin:
        :param invertrelay:
        """
        self._pin = relaypin
        self._invert = invertrelay
        self.wpm = wpm
        wordlensec = 60 / self.wpm

        parislength = floor(258 / 5)
        # the number of divisions in paris sent 5 times in international morse / 5 wpm
        self.dot = wordlensec / parislength
        self.dash = 3 * self.dot
        self.gap = self.dot
        self.lettergap = 3 * self.dot
        self.wordgap = 7 * self.dot - self.lettergap
        self.longdash = 4 * self.dot
        self.zerodash = 5 * self.dot
        self.longgap = 2 * self.dot / 2
        self.sentencegap = self.wordgap

    def playchar(self, char):
        r"""

        :param char:
        :return:
        """
        relay = Relay(pin=self._pin, invert=self._invert)
        for element in char:
            if element == 'W':
                relay.pause(self.wordgap)
            elif element == '.':
                relay.fire(self.dot)
                relay.pause(self.gap)
            elif element == '-':
                relay.fire(self.dash)
                relay.pause(self.gap)
            elif element == 'X':
                relay.fire(self.zerodash)
                relay.pause(self.gap)
            elif element == 'L':
                relay.fire(self.longdash)
                relay.pause(self.gap)
            elif element == 'G':
                relay.pause(self.lettergap)
            else:
                relay.pause(self.sentencegap)  # Ignore other elements
