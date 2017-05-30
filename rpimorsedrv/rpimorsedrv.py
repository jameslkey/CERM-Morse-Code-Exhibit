# coding=utf-8
"""
CERMMorse : rpimorsedrv
5/12/2017 : 3:46 PM
Author : James L. Key
"""
import os
import time

import readconfig

if os.name == 'nt':
    from RPi import GPIO
else:
    import RPi.GPIO as GPIO

__author__ = 'James L. Key'
__project__ = 'CERMMorse'


class IO:
    def __init__(self, config):
        if not isinstance(config, readconfig.Config):
            raise config.ConfigEx('Object is not type readconfig')
        self.GPIO = GPIO
        rpin = config.RelayPin
        dpin = config.MotionDetPin
        self.GPIO.setwarnings(False)
        self.GPIO.setmode(GPIO.BCM)
        self.GPIO.setup(rpin, GPIO.OUT, initial=GPIO.HIGH)
        self.GPIO.setup(dpin, GPIO.IN)


class Relay:
    def __init__(self, config):
        self.config = config
        self.relay = IO(self.config)

    def fire(self, dur):
        self.relay.GPIO.output(self.config.RelayPin, GPIO.LOW)
        time.sleep(dur)
        self.relay.GPIO.output(self.config.RelayPin, GPIO.HIGH)

    def pause(self, dur):
        self.relay.GPIO.output(self.config.RelayPin, GPIO.HIGH)
        time.sleep(dur)


class Detector:
    def __init__(self, config):
        self.config = config
        self.pir = IO(self.config)

    def detect(self):
        print('detecting')
        self.wait_for_motion()
        return

    def wait_for_motion(self):
        while True:
            i = GPIO.input(self.config.MotionDetPin)
            if i == 1:
                break
