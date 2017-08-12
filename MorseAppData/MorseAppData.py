# -*- coding: utf-8 -*-
"""
.. module:: MorseAppData
7/22/2017 : 1:47 PM
:platform: Cross-Platform
:synopsis: Change this text.

.. moduleauthor:: James L. Key <james@bluepenguinslutions.com>

.. todo:: create option to build new default config data file

"""

from .readconfig import MorseConfig
from .trainorder import Trainorder
from .buildfiles import BuildFiles


class MorseAppData(MorseConfig, Trainorder, BuildFiles):
    """
    .. todo:: create option to build new default config data file

    """
    def __init__(self, configpath: str = '', trainorderpath: str = ''):
        MorseConfig.__init__(self, configpath)
        Trainorder.__init__(self, trainorderpath)
        BuildFiles.__init__(self, config_path=configpath, trainorder_path=trainorderpath)

        self.getconfig()
        self.gettrainorder()

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

    def getconfig(self):
        r"""
        Write Comments

        """
        self.readconfig()
        self.color = self.parse_color(self._color_str)

    def gettrainorder(self, toid: int = 1):
        r"""
        Write Comments

        :param toid:

        """
        self.readtrainorder(toid)
        self.station_color = self.parse_color(self._station_color)
