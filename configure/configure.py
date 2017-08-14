# -*- coding: utf-8 -*-
"""
Just a quick note for testing Docstrings.

:module: configure
:program: CERM20
:file: configure
:platform: Cross-Platform
:synopsis: Change this text.

.. moduleauthor:: James L. Key <james@bluepenguinslutions.com>

.. py:currentmodule:: configure

"""


import wx
from configure_gui import GUI


class Application(wx.App):
    """
    Some docs to start off.

    """

    #: Doc comment for class attribute Foo.bar.
    #: It can have multiple lines.
    def __init__(self, redirect=False):
        """
        Start the Foo.

        Args:
            redirect (bool): Unknown.
        """
        wx.App.__init__(self)

        #: Doc comment for instance attribute qux.
        self.qux = 3

        self.spam = 4
        """Docstring for instance attribute spam."""

    def OnInit(self):
        """
        Overloads OnInit from wxPython Application Class

        Returns:
            bool: Success?
        """
        frame = GUI(None)
        frame.Show(True)
        return True


if __name__ == '__main__':

    Application().MainLoop()
