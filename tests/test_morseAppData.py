# -*- coding: utf-8 -*-
"""
Comments go here!!!

:program: CERMMorse
:file: test_morseAppData
:platform: Cross-Platform
:synopsis: Change this text.

.. moduleauthor:: James L. Key <james@bluepenguinslutions.com>

.. py:currentmodule:: Unittests

"""

import os
from unittest import TestCase
import MorseAppData


# Begin
class TestMorseAppData(TestCase):
    def setUp(self):
        config_path = ''
        workorder_path = ''
        self.app_data = MorseAppData.MorseAppData(config_path=config_path,
                                                  workorder_path=workorder_path)

    def test_workorder_color(self):
        self.fail()

    def test_default_color(self):
        self.fail()

    def test__parse_color(self):
        self.fail()

    def test__rev_parse_color(self):
        self.fail()
