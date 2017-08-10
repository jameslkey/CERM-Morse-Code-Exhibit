# -*- coding: utf-8 -*-
"""
:module: configure
:program: CERM20
:file: configure_evt
:platform: Cross-Platform
:synopsis: Change this text.

.. moduleauthor:: James L. Key <james@bluepenguinslutions.com>

.. py:currentmodule:: configure

"""
import wx


class Events:
    def __init__(self, parent):
        self.gui = parent

    def onRed(self, evt):
        self.gui.text.SetBackgroundColour(wx.RED)
        dlg = wx.MessageDialog(self.gui, "Changed colour!. Click on the window to see!", "Successful",
                               style=wx.ICON_INFORMATION | wx.OK)
        dlg.ShowModal()
        if dlg.ShowModal == wx.ID_OK:
            dlg.Destroy()

    def onGreen(self, evt):
        self.gui.text.SetBackgroundColour(wx.GREEN)
        dlg = wx.MessageDialog(self.gui, "Changed colour!. Click on the window to see!", "Successful",
                               style=wx.ICON_INFORMATION | wx.OK)
        dlg.ShowModal()
        if dlg.ShowModal == wx.ID_OK:
            dlg.Destroy()
