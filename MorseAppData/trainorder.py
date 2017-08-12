# -*- coding: utf-8 -*-
"""
Comments go here!!!

Parsing Control for Adafruit_CharLCD in CERMMorse.

:program: CERMMorse
:file: workorder
:platform: Cross-Platform
:synopsis: Change this text.

.. moduleauthor:: James L. Key <james@bluepenguinslutions.com>

.. py:currentmodule:: MorseAppData

-- Frozen JSON is borrowed from  “Fluent Python by Luciano Ramalho (O’Reilly).
-- Copyright 2015 Luciano Ramalho, 978-1-491-94600-8.”

"""

import codecs
import json
import os


try:
    from FrozenJSON import FrozenJSON
except ImportError:
    import sys

    FrozenJSON = sys.modules[__package__ + '.FrozenJSON']


class Trainorder:
    r"""


    """
    def __init__(self, wopath: str = ''):
        r"""

        :param wopath:

        """
        if wopath == '':
            wopath = os.path.dirname(os.getcwd())
            wopath = os.path.join(wopath, 'CERMMorse')
            wopath = os.path.join(wopath, 'data')
            wopath = os.path.join(wopath, 'train_orders.json')
        j_s_o_n = os.path.normpath(wopath)
        if not os.path.exists(j_s_o_n):
            raise WorkorderEx('Work Order File {} does not exists'.format(j_s_o_n))
        with codecs.open(j_s_o_n, 'r', encoding='utf-8') as f:  # Needs encoding to force raspbian to read correctly
            self._rawwodata = json.load(f)
        self._wodata = FrozenJSON(self._rawwodata)
        self.trnordnum = 0
        self.locissued = ''
        self.date = ''
        self.to = ''
        self.at = ''
        self.text = ''
        self.status = 0
        self.time = 0
        self.dispatcher = ''
        self.operator = ''

    def getworkorder(self, woid:  int = 1):
        if woid <= 0:
            raise WorkorderEx('Work Order Number must be Greater than zero')
        if woid > self.numworkorders():
            raise WorkorderEx('Work Order Does not exist in file or file is improperly formatted')
        woid += 1
        self.trnordnum = str(self._wodata.WorkOrder[woid].TONum)
        self.locissued = str(self._wodata.WorkOrder[woid].LocIssued)
        self.date = str(self._wodata.WorkOrder[woid].Date)
        self.to = str(self._wodata.WorkOrder[woid].To)
        self.at = str(self._wodata.WorkOrder[woid].At)
        self.text = str(self._wodata.WorkOrder[woid].Text)
        self.status = str(self._wodata.WorkOrder[woid].Status)
        self.time = str(self._wodata.WorkOrder[woid].Time)
        self.dispatcher = str(self._wodata.WorkOrder[woid].Dispatcher)
        self.operator = str(self._wodata.WorkOrder[woid].Operator)
        self._station_color = str(self._wodata.WorkOrder[woid].StationColor)

    def numworkorders(self) -> int:
        wos = 0
        for _ in self._rawwodata['WorkOrder']:
            wos += 1
        return wos


class WorkorderEx(Exception):
    r"""

    :param message:

    """
    def __init__(self, message: str):
        """

        :param message:
        """
        self.message = message
