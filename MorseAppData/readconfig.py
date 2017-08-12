# -*- coding: utf-8 -*-
"""
Comments go here!!!

.. todo:: create option to build new default config data file

:program: CERMMorse
:file: readonfig
:platform: Cross-Platform
:synopsis: Change this text.

.. moduleauthor:: James L. Key <james@bluepenguinslutions.com>

.. py:currentmodule:: MorseAppData

"""

import json
import os
from .buildfiles import BuildFiles


try:
    from FrozenJSON import FrozenJSON
except ImportError:
    import sys
    FrozenJSON = sys.modules[__package__ + '.FrozenJSON']


class MorseConfig:
    # pylint: disable=R0902

    r"""
    Simply loads config data from a json file and into a class that can be accessed
    by the calling application. Specifically designed for CERMMorse program. It has little to
    no exception handling at present.

    .. todo:: NEED TO REFACTOR CONNECTION TO JSON FILES
    .. todo:: Add Exception to path exists test

    :param configpath:

    """
    def __init__(self, configpath: str = ''):
        self._config_path = configpath
        if self._config_path == '':
            loc_path = os.path.dirname(__file__)
            self._config_path = os.path.join(os.path.sep, loc_path, '..', 'data', 'config.json')
        j_s_o_n = os.path.normpath(self._config_path)

        if not os.path.exists(j_s_o_n):
            pass

        # Needs utf-8 encoding to force raspbian to read correctly
        with open(j_s_o_n, 'r', encoding='utf-8') as file:
            rawconfigdata = json.load(file)
        self._configdata = FrozenJSON(rawconfigdata)

        self.lcd_pin1 = 99
        self.lcd_pin2 = 99
        self.relay_pin = 99
        self.motion_det_pin = 99
        self.wpm = 99
        self.max_wpm = 99
        self.speed_adjust = False
        self._color_str = ''
        self.color = [55, 55, 55]  # set stupid value so it fails its 'get' doesn't work
        self.paragraph_sep = 'XXX'
        self.station_color = False
        # Initialize data
        # self.getconfig()  # get values

    @property
    def config_path(self) -> str:
        r"""
        Property: Path to the MorseConfig JSON file

        :getter: Get MorseConfig.config_path property
        :setter (String): Set MorseConfig.config_path property - Allows changing the file path

        .. todo:: Implement file access as try

        """
        return self._config_path

    @config_path.setter
    def config_path(self, configpath: str):
        r"""
        Setter method for _config_path


        """
        self._config_path = configpath
        if self._config_path == '':
            loc_path = os.path.dirname(__file__)
            self._config_path = os.path.join(os.path.sep, loc_path, '..', 'data')
        self._config_path = os.path.normpath(self._config_path)
        if not os.path.exists(self._config_path):
            buildfiles = BuildFiles(config_path=self._config_path)
            buildfiles.build_config_file()

    def readconfig(self):
        r"""
        Optional method to load the config data into the data again.
        This happens on init of the class, but can be used to load changes,
        if the config file is changed.

        """
        self.lcd_pin1 = int(self._configdata.lcdpins[0].pin1)
        self.lcd_pin2 = int(self._configdata.lcdpins[0].pin2)
        self.relay_pin = int(self._configdata.relaypin[0].pin)
        self.motion_det_pin = int(self._configdata.motiondetectorpin[0].pin)
        self.wpm = int(self._configdata.constants[0].defaultwpm)
        self.max_wpm = int(self._configdata.constants[0].maxwpm)
        self.speed_adjust = bool(self._configdata.general[0].speedadjustbuttonsenabled)
        self._color_str = str(self._configdata.general[0].color)
        self.paragraph_sep = str(self._configdata.general[0].paragraphsep)
        self.station_color_enabled = bool(self._configdata.general[0].stationcolors)
