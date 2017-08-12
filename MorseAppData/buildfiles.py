# -*- coding: utf-8 -*-
"""
Class to build new configuration files.

:program: CERMMorse
:file: buildfiles
:platform: Cross-Platform
:synopsis: Change this text.

.. moduleauthor:: James L. Key <james@bluepenguinslutions.com>

.. py:currentmodule:: MorseAppData

"""

import os
import json

__author__ = 'James L. Key'
__project__ = 'CERM20'


class BuildFiles:

    def __init__(self, config_path: str = '', workorder_path: str = ''):
        self.config_path = config_path
        self.workorder_path = workorder_path

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

        :param color: Color in it's component parts [0, 0, 0]
        :type color: list.
        :returns:  str -- the color decoded to it's name.
        :raises: AttributeError

        """
        # ======================================================
        config_data = [{'constants':
                        [{'defaultwpm': 13, 'maxwpm': 25}],
                        'general':
                            [{'color': 'MAGENTA', 'morseversion': 'AMERICAN',
                              'paragraphsep': '\u00b6', 'speedadjustbuttonsenabled': True}],
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

    def build_workorder_file(self):
        r"""Builds a new properly formatted workorder file.


        :raises: FileError if permission are bad

        """
        work_order_data = [{'trainorder': [{'id': 1,
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
        if self.workorder_path == '':
            loc_path = os.path.dirname(__file__)
            self.workorder_path = os.path.join(os.path.sep, loc_path, '..', 'data')
        self.workorder_path = os.path.normpath(self.workorder_path)
        os.makedirs(self.workorder_path, exist_ok=True)
        self.workorder_path = os.path.join(os.path.sep, self.workorder_path, 'train_orders.json')

        file = open(self.workorder_path, mode='w+', encoding='utf-8')
        json.dump(work_order_data, file, sort_keys=True, indent=4)
        file.flush()
