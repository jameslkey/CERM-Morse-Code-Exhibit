# -*- coding: utf-8 -*-
"""
Comments go here!!!

:program: CERMMorse
:file: trainorder
:platform: Cross-Platform
:synopsis: Change this text.

.. moduleauthor:: James L. Key <james@bluepenguinslutions.com>

.. py:currentmodule:: MorseAppData

-- Frozen JSON is borrowed from  “Fluent Python by Luciano Ramalho (O’Reilly).
-- Copyright 2015 Luciano Ramalho, 978-1-491-94600-8.”

"""

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
    def __init__(self, trainorderpath: str = ''):
        r"""

        :param trainorderpath:

        """
        self._trainorder_path = trainorderpath
        if self._trainorder_path == '':
            loc_path = os.path.dirname(__file__)
            self._trainorder_path = os.path.join(os.path.sep, loc_path, '..', 'data', 'train_orders.json')
        j_s_o_n = os.path.normpath(self._trainorder_path)

        if not os.path.exists(j_s_o_n):
            raise TrainorderEx('Train Order File {} does not exists'.format(j_s_o_n))

        with open(j_s_o_n, 'r', encoding='utf-8') as f:  # Needs encoding to force raspbian to read correctly
            self._rawtodata = json.load(f)
        self._todata = FrozenJSON(self._rawtodata)

        self.trnordnum = 0
        self.locissued = ''
        self.date = ''
        self.to = ''
        self.at = ''
        self.message = ''
        self.status = 0
        self.time = 0
        self.dispatcher = ''
        self.operator = ''
        self._station_color = ''

    def readtrainorder(self, toid:  int = 1):
        r"""
        More comments needed

        :param toid:

        """
        if toid <= 0:
            raise TrainorderEx('Train Order Number must be Greater than zero')
        if toid > self.numtrainorders():
            raise TrainorderEx('Train Order Does not exist in file or file is improperly formatted')
        toid += 1
        self.trnordnum = str(self._todata.trainorder[toid].trnordnum)
        self.locissued = str(self._todata.trainorder[toid].locissued)
        self.date = str(self._todata.trainorder[toid].date)
        self.to = str(self._todata.trainorder[toid].to)
        self.at = str(self._todata.trainorder[toid].at)
        self.message = str(self._todata.trainorder[toid].message)
        self.status = str(self._todata.trainorder[toid].status)
        self.time = str(self._todata.trainorder[toid].time)
        self.dispatcher = str(self._todata.trainorder[toid].dispatcher)
        self.operator = str(self._todata.trainorder[toid].operator)
        self._station_color = str(self._todata.trainorder[toid].stationcolor)

    def numtrainorders(self) -> int:
        r"""
        Comment here

        :return:

        """
        tos = 0
        for _ in self._rawtodata['trainorder']:
            tos += 1
        return tos


class TrainorderEx(Exception):
    r"""
    Yup here too

    .. todo:: Determine if this is needed

    :param message:

    """
    def __init__(self, message: str):
        """

        :param message:
        """
        self.message = message
