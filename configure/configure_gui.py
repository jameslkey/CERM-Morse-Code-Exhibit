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
import wx.adv
from configure_evt import Events


class GUI(wx.Frame):
    def __init__(self, parent):

        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"CERM Morse Code Work Order and Configuration Editor",
                          pos=wx.DefaultPosition, size=wx.Size(600, 650),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        self.functions = Events(self)  # Link to events collection

        bs_main = wx.BoxSizer(wx.VERTICAL)  #

        # Notebook
        self.notebook = wx.Notebook(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        # Workorder Tab scroll Window
        self.sclwin_wo = wx.ScrolledWindow(self.notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           wx.HSCROLL | wx.VSCROLL)
        self.sclwin_wo.SetScrollRate(5, 5)
        # Workorder outer container
        bs_wo_outer = wx.BoxSizer(wx.VERTICAL)

        # Workorder tab splitter
        self.splitter_wo = wx.SplitterWindow(self.sclwin_wo, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D)
        self.splitter_wo.SetSashGravity(0.25)
        self.splitter_wo.Bind(wx.EVT_IDLE, self.functions.splitter_wo_on_idle)

        # Workorder tab left panel
        self.pnl_wo_left = wx.Panel(self.splitter_wo, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        statb_wo_list_outer = wx.StaticBoxSizer(wx.StaticBox(self.pnl_wo_left, wx.ID_ANY, u'Work Order List'),
                                                wx.VERTICAL)
        # Workorder choices
        listbox_wo_choices = [u'Workorder 001', u'Workorder 002', u'Workorder 003']
        self.listbox_wo = wx.ListBox(statb_wo_list_outer.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                     listbox_wo_choices, wx.LB_HSCROLL)
        statb_wo_list_outer.Add(self.listbox_wo, 0, wx.ALL, 5)

        # Workorder Control Buttons
        bs_wo_btns = wx.BoxSizer(wx.VERTICAL)

        self.btn_add_wo = wx.Button(statb_wo_list_outer.GetStaticBox(), wx.ID_ANY, u'Add Workorder', wx.DefaultPosition,
                                    wx.DefaultSize, 0)
        self.btn_add_wo.SetToolTipString(u'Add new workorder')
        self.btn_add_wo.SetMinSize(wx.Size(115, -1))

        bs_wo_btns.Add(self.btn_add_wo, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.btn_delete_wo = wx.Button(statb_wo_list_outer.GetStaticBox(), wx.ID_DELETE, u'Delete Workorder',
                                       wx.DefaultPosition, wx.DefaultSize, 0)
        self.btn_delete_wo.SetToolTipString(u'Delete selected workorder')
        self.btn_delete_wo.SetMinSize(wx.Size(115, -1))

        bs_wo_btns.Add(bs_wo_btns, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        statb_wo_list_outer.Add(bs_wo_btns, 0, wx.TOP, 5)

        self.pnl_wo_left.SetSizer(statb_wo_list_outer)
        self.pnl_wo_left.Layout()
        statb_wo_list_outer.Fit(self.pnl_wo_left)

        # Workorder tab right panel
        self.pnl_wo_right = wx.Panel(self.splitter_wo, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)

        # Workorder data container
        statb_wo_data_outer = wx.StaticBoxSizer(wx.StaticBox(self.pnl_wo_right, wx.ID_ANY, u'Selected Workorder'),
                                                wx.VERTICAL)
        # Workorder data grid
        fgs_wo_data_inner = wx.FlexGridSizer(0, 2, 0, 0)
        fgs_wo_data_inner.SetFlexibleDirection(wx.BOTH)
        fgs_wo_data_inner.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        # Workorder ID
        self.lbl_wo_id = wx.StaticText(statb_wo_data_outer.GetStaticBox(), wx.ID_ANY, u'Work Order ID #:',
                                       wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_wo_id.Wrap(-1)
        fgs_wo_data_inner.Add(self.lbl_wo_id, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.txt_wo_id = wx.TextCtrl(statb_wo_data_outer.GetStaticBox(), wx.ID_ANY, u"001", wx.DefaultPosition,
                                     wx.DefaultSize, wx.TE_READONLY)
        self.txt_wo_id.SetMaxLength(4)
        self.txt_wo_id.SetFont(
            wx.Font(wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD,
                    False, wx.EmptyString))
        self.txt_wo_id.SetToolTipString(u'Current workorder ID')

        fgs_wo_data_inner.Add(self.txt_wo_id, 0, wx.ALL, 5)

        # Train order num
        self.lbl_to_num = wx.StaticText(statb_wo_data_outer.GetStaticBox(), wx.ID_ANY, u'Train Order #:',
                                        wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_to_num.Wrap(-1)
        fgs_wo_data_inner.Add(self.lbl_to_num, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.txt_to_num = wx.TextCtrl(statb_wo_data_outer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                      wx.DefaultSize, 0)
        self.txt_to_num.SetToolTipString(u' Train Order number recorded on workorder slip')

        fgs_wo_data_inner.Add(self.txt_to_num, 0, wx.ALIGN_LEFT | wx.ALL, 5)

        # Location
        self.lbl_loc = wx.StaticText(statb_wo_data_outer.GetStaticBox(), wx.ID_ANY, u'Location Issued:',
                                     wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_loc.Wrap(-1)
        fgs_wo_data_inner.Add(self.lbl_loc, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.txt_loc = wx.TextCtrl(statb_wo_data_outer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                   wx.DefaultSize, 0)
        self.txt_loc.SetToolTipString(u'Where the workorder was issued')
        self.txt_loc.SetMinSize(wx.Size(300, -1))

        fgs_wo_data_inner.Add(self.txt_loc, 0, wx.ALIGN_LEFT | wx.ALL, 5)

        # Date
        self.lbl_date = wx.StaticText(statb_wo_data_outer.GetStaticBox(), wx.ID_ANY, u'Date:', wx.DefaultPosition,
                                      wx.DefaultSize, 0)
        self.lbl_date.Wrap(-1)
        fgs_wo_data_inner.Add(self.lbl_date, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.dp_date = wx.adv.DatePickerCtrl(statb_wo_data_outer.GetStaticBox(), wx.ID_ANY,
                                             wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize,
                                             wx.adv.DP_DEFAULT)
        fgs_wo_data_inner.Add(self.dp_date, 0, wx.ALIGN_LEFT | wx.ALL, 5)

        # Train to whom the workorder is issued
        self.lbl_to = wx.StaticText(statb_wo_data_outer.GetStaticBox(), wx.ID_ANY, u'To Train:', wx.DefaultPosition,
                                    wx.DefaultSize, 0)
        self.lbl_to.Wrap(-1)
        fgs_wo_data_inner.Add(self.lbl_to, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.txt_to = wx.TextCtrl(statb_wo_data_outer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                  wx.DefaultSize, 0)
        self.txt_to.SetToolTipString(u'Train to complete workorder')
        self.txt_to.SetMinSize(wx.Size(300, -1))

        fgs_wo_data_inner.Add(self.txt_to, 0, wx.ALIGN_LEFT | wx.ALL, 5)

        # At location
        self.lbl_at = wx.StaticText(statb_wo_data_outer.GetStaticBox(), wx.ID_ANY, u'At:', wx.DefaultPosition,
                                    wx.DefaultSize, 0)
        self.lbl_at.Wrap(-1)
        fgs_wo_data_inner.Add(self.lbl_at, 0, wx.ALIGN_RIGHT | wx.ALL, 5)





        # self.panel = wx.Panel(self, -1)
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
