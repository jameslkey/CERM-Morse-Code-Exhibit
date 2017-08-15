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
import os
if os.name == 'nt':
    from Waxfruit_CharLCD import Adafruit_CharLCDPlate as Lcd
else:
    import Adafruit_CharLCD as Lcd  # pylint: disable=F0401


class TestLcdScroll(TestCase):
    def setUp(self):
        self.lcd = Lcd.Adafruit_CharLCDPlate()

    def test_message_set(self):
        self.fail()

    def test_message(self):
        self.fail()

    def test_special_characters_set(self):
        self.fail()

    def test_special_characters(self):
        self.fail()

    def test_display_size_set(self):
        self.fail()

    def test_display_size(self):
        self.fail()

    def test_display_cursor_set(self):
        self.fail()

    def test_display_cursor(self):
        self.fail()

    def test_trigger_cursor_set(self):
        self.fail()

    def test_trigger_letter(self):
        self.fail()

    def test_send_character(self):
        self.fail()

    def test_send_word(self):
        self.fail()

    def test_send_message(self):
        self.fail()
