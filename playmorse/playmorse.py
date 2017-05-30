# coding=utf-8
"""
CERMMorse : playmorse
5/12/2017 : 3:46 PM
Author : James L. Key
"""
from math import floor

import rpimorsedrv
# import Adafruit_CharLCD as Lcd
from readconfig import Config

__author__ = 'James L. Key'
__project__ = 'CERMMorse'


class PlayMorse:
    def __init__(self, wpm, config):
        if not isinstance(config, Config):
            raise config.ConfigEx('Object is not type readconfig')
        self.config = config
        self.wpm = wpm
        self.wordlensec = 60 / self.wpm

        self.parislength = floor(258 / 5)
        # the number of divisions in paris sent 5 times in international morse / 5 wpm
        self.dot = self.wordlensec / self.parislength
        self.dash = 3 * self.dot
        self.gap = self.dot
        self.lettergap = 3 * self.dot
        self.wordgap = 7 * self.dot - self.lettergap
        self.longdash = 4 * self.dot
        self.zerodash = 5 * self.dot
        self.longgap = 2 * self.dot / 2
        self.sentencegap = self.wordgap

    def __str__(self):
        return "From PlayMorse:\nwpm is %s\nwordlensec is %s\n" \
               "parislength is %s\n\ndot = %s\ndash = %s\ngap = %s\nlettergap = %s\n" \
               "wordgap = %s\nlongdash = %s\nzerodash = %s\nlonglettergap = %s\n" \
               % (self.wpm, self.wordlensec, self.parislength, self.dot,
                  self.dash, self.gap, self.lettergap, self.wordgap,
                  self.longdash, self.zerodash, self.longgap)

    def __repr__(self):
        return "<wpm: %s\nwordlensec: %s\n" \
               "parislength: %s\n\ndot: %s\ndash: %s\ngap: %s\nlettergap: %s\n" \
               "wordgap: %s\nlongdash: %s\nzerodash = %s\nlonglettergap: %s\n>" % (self.wpm, self.wordlensec,
                                                                                   self.parislength, self.dot,
                                                                                   self.dash, self.gap,
                                                                                   self.lettergap, self.wordgap,
                                                                                   self.longdash, self.zerodash,
                                                                                   self.longgap)

    def play(self, message):

        print(message + ' ')

    def playchar(self, char):
        md = rpimorsedrv.Relay(self.config)
        for element in char:

            if element == 'W':
                md.pause(self.wordgap)
            elif element == '.':
                md.fire(self.dot)
                md.pause(self.gap)
            elif element == '-':
                md.fire(self.dash)
                md.pause(self.gap)
            elif element == 'X':
                md.fire(self.zerodash)
                md.pause(self.gap)
            elif element == 'L':
                md.fire(self.longdash)
                md.pause(self.gap)
            elif element == 'G':
                md.pause(self.lettergap)


if __name__ == '__main__':
    import os

    p = os.path.dirname(os.getcwd())
    p = os.path.join(p, 'CERMMorse')
    p = os.path.join(p, 'data')
    p = os.path.join(p, 'config.json')
    os.path.normpath(p)
    cnf = Config(configpath=p)
    cnf.getconfig()
    pm = PlayMorse(5, cnf)
    print(pm)
    pm.playchar("Test Message. And another Test message. , /")
