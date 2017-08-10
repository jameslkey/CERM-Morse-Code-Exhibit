# -*- coding: utf-8 -*-
"""
Comments go here!!!


:program: CERMMorse
:file: rpimorsedrvrelay
:platform: Cross-Platform
:synopsis: Change this text.

.. moduleauthor:: James L. Key <james@bluepenguinslutions.com>

.. py:currentmodule:: RPiMorseDrv

"""
import os
import time
if os.name == 'nt':
    from RPi import GPIO
else:
    import RPi.GPIO as GPIO

__author__ = 'James L. Key'
__project__ = 'CERM20'


class Relay:
    r"""

    :param pin:
    :param invert:

    """
    def __init__(self, pin: int, invert: bool = False):
        """


        """
        self._pin = pin
        self._invert = invert
        self.RELAY_ON = GPIO.HIGH
        self.RELAY_OFF = GPIO.LOW
        self.GPIO = GPIO
        self.GPIO.setwarnings(False)
        self.GPIO.setmode(GPIO.BCM)
        if self._invert is False:
            self.GPIO.setmode(pin, GPIO.OUT, initial=GPIO.LOW)
        if self._invert is True:
            self.RELAY_ON = GPIO.LOW
            self.RELAY_OFF = GPIO.HIGH
            self.GPIO.setmode(pin, GPIO.OUT, initial=GPIO.HIGH)

    def fire(self, dur: float):
        r"""

        :param dur:
        :return:
        """
        self.GPIO.output(self._pin, self.RELAY_ON)
        time.sleep(dur)
        self.GPIO.output(self._pin, self.RELAY_OFF)

    def pause(self, dur: float):
        r"""

        :param dur:
        :return:
        """
        self.GPIO.output(self._pin, self.RELAY_OFF)
        time.sleep(dur)
