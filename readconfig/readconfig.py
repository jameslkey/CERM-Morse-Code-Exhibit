# coding=utf-8
"""
CERMMorse : readconfig
5/12/2017 : 3:46 PM
Author : James L. Key

Simply loads config data from a json file and into a class that can be accessed 
by the calling application. Specifically designed for CERMMorse program. It has little to 
no exception handling at present.
-- Frozen JSON is borrowed from  “Fluent Python by Luciano Ramalho (O’Reilly).
-- Copyright 2015 Luciano Ramalho, 978-1-491-94600-8.”
"""

import json
import os

try:
    from frozenjson import FrozenJSON
except ImportError:
    import sys

    FrozenJSON = sys.modules[__package__ + '.FrozenJSON']

__author__ = 'James L. Key'
__project__ = 'CERMMorse'


class Config:
    def __init__(self, configpath=''):
        if configpath == '':
            configpath = os.path.dirname(os.getcwd())
            configpath = os.path.join(configpath, 'CERMMorse')
            configpath = os.path.join(configpath, 'data')
            configpath = os.path.join(configpath, 'config.json')
        j_s_o_n = os.path.normpath(configpath)
        if not os.path.exists(j_s_o_n):
            raise ConfigEx('Config File {} does not exists'.format(j_s_o_n))
        with open(j_s_o_n, 'r', encoding='utf-8') as f:  # Needs encoding to force raspbian to read correctly
            rawconfigdata = json.load(f)
        self._configdata = FrozenJSON(rawconfigdata)

        self.LCDPin1 = 99
        self.LCDPin2 = 99
        self.RelayPin = 99
        self.MotionDetPin = 99
        self.WPM = 99
        self.MaxWPM = 99
        self.SpeedAdjust = False
        self._Colorstr = ''
        self.Color = (55, 55, 55)  # set stupid value so it fails its 'get' doesn't work
        self.ParagraphSep = 'XXX'

    def getconfig(self):
        self.LCDPin1 = int(self._configdata.LCDPins[0].Pin1)
        self.LCDPin2 = int(self._configdata.LCDPins[0].Pin2)
        self.RelayPin = int(self._configdata.RelayPin[0].Pin)
        self.MotionDetPin = int(self._configdata.MotionDetectorPin[0].Pin)
        self.WPM = int(self._configdata.Constants[0].DefaultWPM)
        self.MaxWPM = int(self._configdata.Constants[0].MaxWPM)
        self.SpeedAdjust = bool(self._configdata.General[0].SpeedAdjustButtonsEnabled)
        self._Colorstr = str(self._configdata.General[0].Color)
        self.Color = self.parseColor()
        self.ParagraphSep = str(self._configdata.General[0].ParagraphSep)

    def parseColor(self):
        if self._Colorstr == "RED":
            Color = [1, 0, 0]
        elif self._Colorstr == "GREEN":
            Color = [0, 1, 0]
        elif self._Colorstr == "BLUE":
            Color = [0, 0, 1]
        elif self._Colorstr == "YELLOW":
            Color = [1, 1, 0]
        elif self._Colorstr == "CYAN":
            Color = [0, 1, 1]
        elif self._Colorstr == "MAGENTA":
            Color = [1, 0, 1]
        elif self._Colorstr == "WHITE":
            Color = [1, 1, 1]
        else:
            Color = [99, 99, 99]  # Fail Spectacularly
        return Color


class ConfigEx(Exception):
    def __init__(self, message):
        self.message = message
