# coding=utf-8
"""
CERMMorse : Morse
5/12/2017 : 3:46 PM
Author : James L. Key
Connecticut Eastern Railroad Museum Exhibit Software
"""

import argparse
import os
import time
from random import randrange

import pymorse
import readconfig
import rpimorsedrv
from playmorse import PlayMorse
from workorder import WorkOrder

if os.name == 'nt':
    import Waxfruit_CharLCD as Lcd
    from Adafruit_CharLCD import RIGHT, UP, DOWN, LEFT, SELECT
else:
    import Adafruit_CharLCD as Lcd
    from Adafruit_CharLCD import RIGHT, UP, DOWN, LEFT, SELECT
__author__ = 'James L. Key'
__project__ = 'CERMMorse'  # Connecticut Eastern Railroad Museum


class CERMMorse:
    def __init__(self, configpath, wopath):
        # The program loads any config information from config file
        # Also do house keeping setup

        if configpath is None:
            configpath = os.path.dirname(os.getcwd())
            configpath = os.path.join(configpath, 'CERM-Morse-Code-Exhibit')
            configpath = os.path.join(configpath, 'data')
            configpath = os.path.join(configpath, 'config.json')
        self._configpath = os.path.normpath(configpath)

        if wopath is None:
            wopath = os.path.dirname(os.getcwd())
            wopath = os.path.join(wopath, 'CERMMorse')
            wopath = os.path.join(wopath, 'data')
            wopath = os.path.join(wopath, 'work_orders.json')
        self._wopath = os.path.normpath(wopath)

        self.conf = readconfig.Config(self._configpath)
        self.conf.getconfig()

        self.lcd = Lcd.Adafruit_CharLCDPlate()
        self.lcd.create_char(0, [0, 0, 15, 29, 29, 13, 5, 5])  # Pilcrow
        self.lcd.create_char(1, [0, 27, 9, 9, 0, 0, 0, 0])  # Left Double Quote
        self.lcd.create_char(2, [0, 27, 18, 18, 0, 0, 0, 0])  # Right Double Quote
        self.lcd.create_char(3, [0, 2, 6, 14, 6, 2, 0, 0])  # Left Arrow
        self.lcd.create_char(4, [0, 8, 12, 14, 12, 8, 0, 0])  # Right Arrow
        self.lcd.create_char(5, [0, 0, 4, 14, 31, 0, 0, 0])  # Up Arrow
        self.lcd.create_char(6, [0, 0, 31, 14, 4, 0, 0, 0])  # Down Arrow
        self.lcd.autoscroll(False)
        self.lcd.enable_display(1)
        self._charbuffer = []
        self._paragraph_sep = '\u00B6'

    def welcome(self):
        self.lcd.set_backlight(1)
        self.lcd.set_color(0, 1, 0)

        # Display welcome message to prove we are at least starting
        self.lcd.set_cursor(0, 0)
        self.lcd.message("Welcome to CERM")
        self.lcd.set_cursor(0, 1)
        self.lcd.message("Morse Display")
        time.sleep(5)
        #  Shutoff display
        self.lcd.clear()
        self.lcd.set_backlight(0)

    def run(self):

        # Program starts thread to monitor button presses to adjust speed
        # seems that threading ans i2c don't mix... maybe add speed adjust to character write loop

        # Load messages
        self.welcome()
        wol = WorkOrder(self._wopath)

        # Wait for someone to move/come in/what ever
        while True:
            det = rpimorsedrv.Detector(self.conf)
            self.lcd.set_backlight(0)
            self.lcd.clear()
            print(self.conf.WPM)
            det.detect()

            # Start Display
            self.lcd.set_backlight(1)
            self.lcd.set_color(self.conf.Color[0], self.conf.Color[1], self.conf.Color[2])

            # Select message to play
            msgnum = self.selectmessage(wol)
            self.getmessage(wol, msgnum)

            # Encode message to code
            trans = pymorse.Morse()
            tonum_morse = trans.morseencode('ORDER NUMBER:' + wol.TONum)
            locissued_morse = trans.morseencode('LOCATION:' + wol.LocIssued)
            date_morse = trans.morseencode("DATE:" + wol.Date)
            to_morse = trans.morseencode('TO:' + wol.To)
            at_morse = trans.morseencode('AT:' + wol.At)
            text_morse = trans.morseencode('WO:' + wol.Text)
            status_morse = trans.morseencode('STATUS:' + wol.Status)
            time_morse = trans.morseencode('TIME:' + wol.Time)
            dispatcher_morse = trans.morseencode('DISPATCHER:' + wol.Dispatcher)
            operator_morse = trans.morseencode('OP:' + wol.Operator)
            paragraph_sep_morse = trans.morseencode(self._paragraph_sep)

            completemessage = self.assemblemessage(paragraph_sep_morse, tonum_morse, locissued_morse, date_morse,
                                                   to_morse, at_morse, text_morse, status_morse, time_morse,
                                                   dispatcher_morse, operator_morse)

            # Display message and Play message one character at a time until message done
            self.sendmessage(completemessage)
            # Shutoff Display
            # time.sleep(5)
            self.lcd.set_backlight(0)

            # Repeat from Wait for person

    @staticmethod
    def getmessage(woobj, msgnum=1):
        woobj.getworkorder(msgnum)
        return woobj

    @staticmethod
    def selectmessage(woobj):
        msgnum = randrange(1, woobj.numworkorders())
        return msgnum

    @staticmethod
    def assemblemessage(parasep, *args):
        completemessage = ''
        for arg in args:
            completemessage = completemessage + arg + parasep
        return completemessage

    def sendmessage(self, message):
        pm = PlayMorse(self.conf.WPM, self.conf)
        trans = pymorse.Morse()

        for char in message.split('~'):
            display = trans.morsedecode(str(char))
            pm.playchar(char)
            self.displaychar(display)

            if self.conf.SpeedAdjust is True:
                if self.checkadjustspeed():
                    break  # If speed adjustment change pop out and restart

    def checkadjustspeed(self):
        if self.lcd.is_pressed(UP):
            if self.conf.WPM <= self.conf.MaxWPM:
                self.conf.WPM += 1
            return True
        if self.lcd.is_pressed(DOWN):
            if self.conf.WPM >= 5:
                self.conf.WPM -= 1
            return True
        return False

    def displaychar(self, char):
        # Process for special Characters
        if not char:  # catch null characters
            return
        if char == '\u00B6':  # Pilcrow
            char = '\x00'
        if char == '\u201C':  # Open left double quote
            char = '\x01'
        if char == '\u201D':  # Close right double quote
            char = '\x02'
        if len(self._charbuffer) == 0:
            self.lcd.set_cursor(0, 1)
        if not char == ' ':
            self.lcd.message(char)
            self._charbuffer.append(char)
        if len(self._charbuffer) >= 15 or char == ' ' or char == '\x00' or char == ':':
            self.lcd.clear()
            if self._charbuffer: 
                self.lcd.message(self._charbuffer)
            self._charbuffer.clear()


def main():
    parser = argparse.ArgumentParser(description='CERM Morse interactive demonstration.')
    parser.add_argument('--config', help='Config File -- Default data/config.json', dest='configpath')
    parser.add_argument('--workorder', help='Workorder file -- Default data/work_orders.json', dest='wopath')
    args = parser.parse_args()
    cerm = CERMMorse(configpath=args.configpath, wopath=args.wopath)
    cerm.run()


# Start
main()
