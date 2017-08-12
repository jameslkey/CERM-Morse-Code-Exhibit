# -*- coding: utf-8 -*-
"""
Comments go here!!!

:program: CERMMorse
:file: test_trainorder
:platform: Cross-Platform
:synopsis: Change this text.

.. moduleauthor:: James L. Key <james@bluepenguinslutions.com>

.. py:currentmodule:: Unittests

"""

from MorseAppData import MorseAppData
from unittest import TestCase
import os


class TestTrainorder(TestCase):
    def setUp(self):
        loc_path = os.path.dirname(__file__)
        trainorder_file = os.path.join(os.path.sep, loc_path, '..', 'data', 'train_orders.json')
        trainorder_file = os.path.normpath(trainorder_file)
        self.trainorder = MorseAppData(trainorderpath=trainorder_file)
        self.trainorder.gettrainorder()

    def test_gettrainorder(self):
        self.fail()

    def test_numtrainorders(self):
        self.fail()
