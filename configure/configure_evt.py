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
from wx.lib.wordwrap import wordwrap
import wx.adv


class Events:
    def __init__(self, parent):
        self.gui = parent

    def on_notebook_tab_change(self, event):
        event.Skip()

    def on_btn_add_to(self, event):
        event.Skip()

    def on_btn_delete_to(self, event):
        event.Skip()

    def on_btn_clear_to_data(self, event):
        event.Skip()

    def on_btn_undo_to_data(self, event):
        event.Skip()

    def on_btn_save_to_data(self, event):
        event.Skip()

    def wpm_update(self, event):
        event.Skip()

    def on_menuitem_new_to(self, event):
        event.Skip()

    def on_menuitme_new_conf(self, event):
        event.Skip()

    def on_menuitem_open_to(self, event):
        event.Skip()

    def on_menuitem_open_conf(self, event):
        event.Skip()

    def on_menuitem_save_to(self, event):
        event.Skip()

    def on_menuitem_save_conf(self, event):
        event.Skip()

    def on_menuitem_save_all(self, event):
        event.Skip()

    def on_menuitem_save_to_as(self, event):
        event.Skip()

    def on_menuitem_save_conf_as(self, event):
        event.Skip()

    def on_menuitem_exit(self, event):
        event.Skip()

    def on_menuitem_undo(self, event):
        event.Skip()

    def on_menuitem_redo(self, event):
        event.Skip()

    def on_menuitem_cut(self, event):
        event.Skip()

    def on_menuitem_copy(self, event):
        event.Skip()

    def on_menuitem_paste(self, event):
        event.Skip()

    def on_menuitem_about(self, event):
        event.Skip()

    def splitter_to_on_idle(self, event):
        self.gui.SetSashPosition(135)
        self.gui.Unbind(wx.EVT_IDLE)
