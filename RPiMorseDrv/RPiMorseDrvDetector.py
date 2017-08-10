# -*- coding: utf-8 -*-
"""
Comments go here!!!


:program: CERMMorse
:file: rpimorsedrvdetector
:platform: Cross-Platform
:synopsis: Change this text.

.. moduleauthor:: James L. Key <james@bluepenguinslutions.com>

.. py:currentmodule:: RPiMorseDrv

"""

import os
if os.name == 'nt':
    from RPi import GPIO
else:
    import RPi.GPIO as GPIO

__author__ = 'James L. Key'
__project__ = 'CERM20'


class Detector:
    r"""

    """
    def __init__(self, pin: int):
        r"""

        :param pin:
        """
        self.GPIO = GPIO
        self._pin = pin
        self.GPIO.setwarnings(False)
        self.GPIO.setmode(GPIO.BCM)
        self.GPIO.setup(pin, GPIO.IN)

    def detect(self):
        """

        :return:
        """
        while True:
            control = self.GPIO.input(self._pin)
            if control == 1:
                break

