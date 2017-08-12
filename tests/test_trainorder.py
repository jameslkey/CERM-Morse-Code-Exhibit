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
from random import randrange
import os


class TestTrainorder(TestCase):
    def setUp(self):
        loc_path = os.path.dirname(__file__)
        trainorder_file = os.path.join(os.path.sep, loc_path, '..', 'data', 'train_orders.json')
        trainorder_file = os.path.normpath(trainorder_file)
        self.trainorder = MorseAppData(trainorderpath=trainorder_file)
        self.trainorder.gettrainorder()

    def test_gettrainorder(self):
        """

        .. todo:: WRITE A REAL TEST

        """
        self.trainorder.gettrainorder(toid=randrange(1, self.trainorder.numtrainorders()))

    def test_numtrainorders(self):
        self.assertGreaterEqual(self.trainorder.numtrainorders(), 1,
                                'Train Order Number not positive and greater than zero!')
