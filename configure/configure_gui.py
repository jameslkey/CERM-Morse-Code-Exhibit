# -*- coding: utf-8 -*-
"""
:module: configure
:program: CERM20
:file: configure_gui
:platform: Cross-Platform
:synopsis: Change this text.

.. moduleauthor:: James L. Key <james@bluepenguinslutions.com>

.. py:currentmodule:: configure

"""
import wx
from configure_evt import Events


class GUI(wx.Frame):
    def __init__(self, parent):

        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"CERM Morse Code Work Order and Configuration Editor",
                          pos=wx.DefaultPosition, size=wx.Size(600, 650),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        self.functions = Events(self)
        self.panel = wx.Panel(self, -1)
        # add two buttons and text control
        self.text = wx.TextCtrl(self.panel, -1)
        self.text.SetBackgroundColour(wx.BLACK)
        self.button1 = wx.Button(self.panel, -1, "Red Colour")
        self.button2 = wx.Button(self.panel, -1, "Green Colour")
        # bind events to widgets
        self.Bind(wx.EVT_BUTTON, self.functions.onRed, id=self.button1.GetId())
        self.Bind(wx.EVT_BUTTON, self.functions.onGreen, id=self.button2.GetId())
        # add them to sizer [define it first to prevent python automatic detector to find you red handed]
        main = wx.BoxSizer(wx.VERTICAL)
        main.Add(self.text, 1, wx.EXPAND | wx.ALL, 1)
        # add buttons in separate sizer
        sub_main = wx.BoxSizer(wx.HORIZONTAL)
        sub_main.Add(self.button1, 0, wx.EXPAND | wx.ALL, 5)
        sub_main.Add(self.button2, 0, wx.EXPAND | wx.ALL, 5)
        main.Add(sub_main, 0, wx.EXPAND | wx.ALL, 5)
        # set sizers to Frame through panel
        self.panel.SetSizer(main)
        self.panel.Layout()
