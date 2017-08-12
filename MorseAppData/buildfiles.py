# -*- coding: utf-8 -*-
"""
Class to encapsulate routines to build fresh or missing data files for CERMMorse Application.

:program: CERMMorse
:file: buildfiles
:platform: Cross-Platform
:synopsis: Data file builder.

.. moduleauthor:: James L. Key <james@bluepenguinslutions.com>

.. py:currentmodule:: MorseAppData

"""

import os
import json

__author__ = 'James L. Key'
__project__ = 'CERM20'


class BuildFiles:
    r"""
    Routines to build fresh or missing data files for CERMMorse Application

    """

    def __init__(self, config_path: str = '', trainorder_path: str = ''):
        self.config_path = config_path
        self.trainorder_path = trainorder_path

    @property
    def config_path(self):
        """

        :return:

        """
        return self.config_path

    @config_path.setter
    def config_path(self, config_path: str = ''):
        """

        :param config_path:

        """

    def build_config_file(self):
        r"""This function does something.
        Builds a nice new config.json file with default values.

        :raises: FileError if permission are bad

        """
        # ======================================================
        config_data = [{'constants':
                        [{'defaultwpm': 13, 'maxwpm': 25}],
                        'general':
                            [{'color': 'MAGENTA', 'morseversion': 'AMERICAN',
                              'paragraphsep': '\u00b6', 'speedadjustbuttonsenabled': True,
                              'stationcolor': True}],
                        'lcdpins': [{'pin1': 2, 'pin2': 3}],
                        'motiondetectorpin': [{'pin': 20}],
                        'relaypin': [{'pin': 26}]}]

        # =======================================================
        if self.config_path == '':
            loc_path = os.path.dirname(__file__)
            self.config_path = os.path.join(os.path.sep, loc_path, '..', 'data')
        self.config_path = os.path.normpath(self.config_path)
        os.makedirs(self.config_path, exist_ok=True)

        self.config_path = os.path.join(os.path.sep, self.config_path, 'config.json')
        file = open(self.config_path, mode='w+', encoding='utf-8')
        json.dump(config_data, file, sort_keys=True, indent=4)
        file.flush()

    def build_trainorder_file(self):
        r"""Builds a new properly formatted workorder file.


        :raises: FileError if permission are bad

        """
        # ======================================================
        train_order_data = [{'trainorder': [{'id': 1,
                                             'trnordnum': 11,
                                             'locissued': 'Salem Yd',
                                             'date': '11-02-1944',
                                             'to': 'C&E Extra 2005 North',
                                             'at': 'VN Tower',
                                             'message': 'No 123 Eng 1001 take siding meet Extra 2005'
                                                     ' North at Kell instead of Texico. take siding'
                                                     ' meet No 174 Eng 895 and Extra 1937 North at'
                                                     ' Benton. No 122 Eng 222 take siding meet'
                                                     ' No 123 Eng 1001 at Texico. ',
                                             'status': 'MadeComplete',
                                             'time': '0659',
                                             'dispatcher': 'RED',
                                             'operator': 'Cole',
                                             'stationcolor': 'BLUE'}]}]
        # =======================================================
        if self.trainorder_path == '':
            loc_path = os.path.dirname(__file__)
            self.trainorder_path = os.path.join(os.path.sep, loc_path, '..', 'data')
        self.trainorder_path = os.path.normpath(self.trainorder_path)
        os.makedirs(self.trainorder_path, exist_ok=True)
        self.trainorder_path = os.path.join(os.path.sep, self.trainorder_path, 'train_orders.json')

        file = open(self.trainorder_path, mode='w+', encoding='utf-8')
        json.dump(train_order_data, file, sort_keys=True, indent=4)
        file.flush()
