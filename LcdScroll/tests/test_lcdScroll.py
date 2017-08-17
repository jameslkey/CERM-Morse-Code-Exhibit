# -*- coding: utf-8 -*-
"""
Comments go here!!!

:program: CERMMorse2.0
:file: test_lcdScroll
:platform: Cross-Platform
:synopsis: Change this text.

.. moduleauthor:: James L. Key <james@bluepenguinslutions.com>

"""
from unittest import TestCase
from LcdScroll import LcdScroll
from unittest import skip
from LcdScroll import LcdScrollEx

import os
if os.name == 'nt':
    from Waxfruit_CharLCD import Adafruit_CharLCDPlate
else:
    from Adafruit_CharLCD import Adafruit_CharLCDPlate  # pylint: disable=F0401


class TestLcdScroll(TestCase):
    def setUp(self):
        self.display = Adafruit_CharLCDPlate(cols=16, lines=2)
        self.lcd = LcdScroll(self.display)

    def test_message_set(self):
        """
        Simple test of message set method

        """
        self.lcd.message = 'Test message that should be longer than 16 characters'
        self.assertIsInstance(self.lcd.message, str)

    def test_message(self):
        """
        Simple test of message get method

        """
        self.lcd.message = 'Test message that should be longer than 16 characters'
        self.assertIsInstance(self.lcd.message, str)

    @skip
    def test_special_characters_set(self):
        self.fail()

    @skip
    def test_special_characters(self):
        self.fail()

    def test_display_size_set(self):
        """
        Simple test of size set method

        """
        self.lcd.columns = 20
        self.lcd.lines = 4
        self.assertIsInstance(self.lcd.display_size, tuple, 'Did not return tuple')
        self.assertEqual(self.lcd.display_size, (20, 4), 'Unable to set display size')
        self.lcd.columns = 16
        self.lcd.lines = 2
        self.assertEqual(self.lcd.display_size, (16, 2), 'Unable to change display size')

        def setcol():
            self.lcd.columns = 0

        def setline():
            self.lcd.lines = -3

        self.assertRaises(LcdScrollEx, setcol)
        self.assertRaises(LcdScrollEx, setline)

    def test_display_size(self):
        """
        Simple test of size get method

        """
        self.assertIsInstance(self.lcd.display_size, tuple, 'Did not return tuple')

    @skip
    def test_display_cursor_set(self):
        self.fail()

    @skip
    def test_display_cursor(self):
        self.fail()

    @skip
    def test_trigger_cursor_set(self):
        self.fail()

    @skip
    def test_trigger_letter(self):
        self.fail()

    @skip
    def test_send_character(self):
        self.fail()

    @skip
    def test_send_word(self):
        self.fail()

    @skip
    def test_send_message(self):
        self.fail()

