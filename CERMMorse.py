# -*- coding: utf-8 -*-
"""
Just a quick note for testing Docstrings.

:program: CERMMorse
:file: CERMMorse
:platform: Cross-Platform
:synopsis: Change this text.

.. moduleauthor:: James L. Key <james@bluepenguinslutions.com>

.. py:currentmodule:: CERMMorse

"""


import argparse
import os
import time
from random import randrange

import PyMorse
import RPiMorseDrv
from PlayMorse import PlayMorse
from MorseAppData import MorseAppData

if os.name == 'nt':
    import Waxfruit_CharLCD as Lcd
    from Adafruit_CharLCD import RIGHT, UP, DOWN, LEFT, SELECT
else:
    import Adafruit_CharLCD as Lcd
    from Adafruit_CharLCD import RIGHT, UP, DOWN, LEFT, SELECT
__author__ = 'James L. Key'
__project__ = 'CERMMorse'  # Connecticut Eastern Railroad Museum


class CERMMorse:
    def __init__(self, configpath, trainorderpath):
        # The program loads any config information from config file
        # Also do house keeping setup

        self._config_path = configpath
        if self._config_path == '':
            loc_path = os.path.dirname(__file__)
            self._config_path = os.path.join(os.path.sep, loc_path, 'data', 'config.json')
        self._config_path = os.path.normpath(self._config_path)

        self._trainorder_path = trainorderpath
        if self._trainorder_path == '':
            loc_path = os.path.dirname(__file__)
            self._trainorder_path = os.path.join(os.path.sep, loc_path, 'data', 'train_orders.json')
        self._train_order_path = os.path.normpath(self._trainorder_path)

        self.morse_data = MorseAppData(configpath=self._config_path, trainorderpath=self._train_order_path)
        self.morse_data.getconfig()

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

        # Load messages
        self.welcome()

        # Wait for someone to move/come in/what ever
        while True:
            det = RPiMorseDrv.Detector(self.morse_data.motion_det_pin)
            self.lcd.set_backlight(0)
            self.lcd.clear()
            print(self.morse_data.wpm)
            det.detect()

            # Start Display
            self.lcd.set_backlight(1)
            self.lcd.set_color(self.morse_data.color[0], self.morse_data.color[1], self.morse_data.color[2])

            # Select message to play
            msgnum = self.selectmessage()
            self.morse_data.gettrainorder(msgnum)

            if self.morse_data.station_color_enabled is True:
                self.disp_color = self.morse_data.parse_color(self.morse_data.station_color)
            # Encode message to code
            trans = PyMorse.Morse()
            tonum_morse = trans.morseencode('ORDER NUMBER:' + self.morse_data.trnordnum)
            locissued_morse = trans.morseencode('LOCATION:' + self.morse_data.locissued)
            date_morse = trans.morseencode("DATE:" + self.morse_data.date)
            to_morse = trans.morseencode('TO:' + self.morse_data.to)
            at_morse = trans.morseencode('AT:' + self.morse_data.at)
            text_morse = trans.morseencode('WO:' + self.morse_data.message)
            status_morse = trans.morseencode('STATUS:' + self.morse_data.status)
            time_morse = trans.morseencode('TIME:' + self.morse_data.time)
            dispatcher_morse = trans.morseencode('DISPATCHER:' + self.morse_data.dispatcher)
            operator_morse = trans.morseencode('OP:' + self.morse_data.operator)
            paragraph_sep_morse = trans.morseencode(self.morse_data.paragraph_sep)

            completemessage = self.assemblemessage(paragraph_sep_morse, tonum_morse, locissued_morse, date_morse,
                                                   to_morse, at_morse, text_morse, status_morse, time_morse,
                                                   dispatcher_morse, operator_morse)

            # Display message and Play message one character at a time until message done
            if self.morse_data.station_color_enabled is True:
                self.lcd.set_color(self.disp_color[0], self.disp_color[1], self.disp_color[2])
            self.sendmessage(completemessage)
            # Shutoff Display
            # time.sleep(5)
            self.lcd.set_backlight(0)

            # Repeat from Wait for person

    def selectmessage(self):
        msgnum = randrange(1, self.morse_data.numtrainorders())
        return msgnum

    @staticmethod
    def assemblemessage(parasep, *args):
        completemessage = ''
        for arg in args:
            completemessage = completemessage + arg + parasep
        return completemessage

    def sendmessage(self, message):
        pm = PlayMorse(self.morse_data.wpm, self.morse_data.relay_pin)
        trans = PyMorse.Morse()

        for char in message.split('~'):
            display = trans.morsedecode(str(char))
            pm.playchar(char)
            self.displaychar(display)

            if self.morse_data.speed_adjust and self.checkadjustspeed():
                    break  # If speed adjustment change pop out and restart

    def checkadjustspeed(self):
        if self.lcd.is_pressed(UP):
            if self.morse_data.wpm <= self.morse_data.max_wpm:
                self.morse_data.wpm += 1
            return True
        if self.lcd.is_pressed(DOWN):
            if self.morse_data.wpm >= 5:
                self.morse_data.wpm -= 1
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
    parser.add_argument('--config', help='Config File -- Default data/config.json', dest='config_path')
    parser.add_argument('--trainorder', help='Trainorder file -- Default data/train_orders.json', dest='to_path')
    args = parser.parse_args()
    cerm = CERMMorse(configpath=args.config_path, trainorderpath=args.to_path)
    cerm.run()


# Start
main()

