# -*- coding: utf-8 -*-
"""
Just a quick note for testing Docstrings.

:program: CERMMorse
:file: CERMMorse
:platform: Cross-Platform
:synopsis: Change this text.

.. moduleauthor:: James L. Key <james@bluepenguinslutions.com>

.. py:currentmodule:: CERMMorse

"""

import os
if os.name == 'nt':
    import Waxfruit_CharLCD as Lcd
else:
    import Adafruit_CharLCD as Lcd  # pylint: disable=F0401


class CERMMorse:
    r"""

    """

    def __init__(self):
        """

        """
        self.lcd = Lcd.Adafruit_CharLCDPlate()


def main():
    r"""

    :return:
    """
    pass

if __name__ == '__main__':
    main()
