# -*- coding: utf-8 -*-
"""
.. module:: MorseAppData
7/22/2017 : 1:47 PM
:platform: Cross-Platform
:synopsis: Change this text.

.. moduleauthor:: James L. Key <james@bluepenguinslutions.com>

.. todo:: create option to build new default config data file

"""

from .readconfig import MorseConfig as MorseConfig
from .workorder import Workorder as WorkOrder


class MorseAppData(MorseConfig, WorkOrder):
    """
    .. todo:: create option to build new default config data file

    """
    def __init__(self, config_path, workorder_path):
        MorseConfig.__init__(self, config_path)
        WorkOrder.__init__(self, workorder_path)
        self._conf_color_str = MorseConfig._color_strcolor
        self._wo_color_str = WorkOrder._station_color

    @property
    def workorder_color(self) -> list:
        color = self.parse_color(self._wo_color_str)
        return color

    @workorder_color.setter
    def workorder_color(self, color: list):
        # Todo: create validation
        self.rev_parse_color(color)

    @property
    def default_color(self) -> list:
        color = self.parse_color(self._conf_color_str)
        return color

    @default_color.setter
    def default_color(self, color: list):
        # Todo: create validation
        self.rev_parse_color(color)

    @staticmethod
    def parse_color(color_str: str) -> list:
        r"""
        .. todo:: Fix comment

        Semi-Private method that reads the private _color_str variable,
        which is a String containing the name of the color.
        It returns a list of the RGB values,
        in this case ons and offs for each value represented by 0 and 1.

        :return color:

        """
        if color_str == "RED":
            color = [1, 0, 0]
        elif color_str == "GREEN":
            color = [0, 1, 0]
        elif color_str == "BLUE":
            color = [0, 0, 1]
        elif color_str == "YELLOW":
            color = [1, 1, 0]
        elif color_str == "CYAN":
            color = [0, 1, 1]
        elif color_str == "MAGENTA":
            color = [1, 0, 1]
        elif color_str == "WHITE":
            color = [1, 1, 1]
        else:
            color = [99, 99, 99]  # Fail Spectacularly
        return color

    @staticmethod
    def rev_parse_color(color: list) -> str:
        r"""This function does something.

        .. todo:: Add comment

        :param color: Color in it's component parts [0, 0, 0]
        :type color: list.
        :returns:  str -- the color decoded to it's name.
        :raises: AttributeError

        """
        if color == [1, 0, 0]:
            color_str = "RED"
        elif color == [0, 1, 0]:
            color_str = "GREEN"
        elif color == [0, 0, 1]:
            color_str = "BLUE"
        elif color == [1, 1, 0]:
            color_str = "YELLOW"
        elif color == [0, 1, 1]:
            color_str = "CYAN"
        elif color == [1, 0, 1]:
            color_str = "MAGENTA"
        else:  # [1, 1, 1]
            color_str = "WHITE"
        return color_str
