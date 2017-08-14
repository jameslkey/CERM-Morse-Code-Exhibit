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

        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u'CERM Morse Code Train Order and Configuration Editor',
                          pos=wx.DefaultPosition, size=wx.Size(650, 650),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        self.functions = Events(self)  # Link to events collection

        bs_main = wx.BoxSizer(wx.VERTICAL)  # Overall Sizer to contain notebook

        # Notebook
        self.notebook = wx.Notebook(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        # Trainorder Tab scroll Window
        self.scrlwin_to = wx.ScrolledWindow(self.notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                            wx.HSCROLL | wx.VSCROLL)
        self.scrlwin_to.SetScrollRate(5, 5)
        # Trainorder outer container
        bs_to_outer = wx.BoxSizer(wx.VERTICAL)

        # Trainorder tab splitter
        self.splitter_to = wx.SplitterWindow(self.scrlwin_to, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D |
                                             wx.SP_LIVE_UPDATE)
        self.splitter_to.SetSashGravity(0.25)
        # self.splitter_to.Bind(wx.EVT_, self.functions.splitter_to_on_idle)

        # Trainorder tab left panel
        self.pnl_to_left = wx.Panel(self.splitter_to, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        statb_to_list_outer = wx.StaticBoxSizer(wx.StaticBox(self.pnl_to_left, wx.ID_ANY, u'Train Order List'),
                                                wx.VERTICAL)
        # Trainorder choices
        listbox_to_choices = [u'Trainorder 001', u'Trainorder 002', u'Trainorder 003']
        self.listbox_to = wx.ListBox(statb_to_list_outer.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                     listbox_to_choices, wx.LB_HSCROLL)
        statb_to_list_outer.Add(self.listbox_to, 0, wx.ALL, 5)

        # Trainorder Control Buttons
        bs_to_list_btns = wx.BoxSizer(wx.VERTICAL)
        self.btn_add_to = wx.Button(statb_to_list_outer.GetStaticBox(), wx.ID_ANY, u'Add Trainorder',
                                    wx.DefaultPosition, wx.DefaultSize, 0)
        self.btn_add_to.SetToolTip(u'Add new trainorder')
        self.btn_add_to.SetMinSize(wx.Size(115, -1))
        bs_to_list_btns.Add(self.btn_add_to, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.btn_delete_to = wx.Button(statb_to_list_outer.GetStaticBox(), wx.ID_DELETE, u'Delete Trainorder',
                                       wx.DefaultPosition, wx.DefaultSize, 0)
        self.btn_delete_to.SetToolTip(u'Delete selected trainorder')
        self.btn_delete_to.SetMinSize(wx.Size(115, -1))
        bs_to_list_btns.Add(self.btn_delete_to, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        statb_to_list_outer.Add(bs_to_list_btns, 0, wx.TOP, 5)

        self.pnl_to_left.SetSizer(statb_to_list_outer)
        self.pnl_to_left.Layout()
        statb_to_list_outer.Fit(self.pnl_to_left)

        # Trainorder tab right panel
        self.pnl_to_right = wx.Panel(self.splitter_to, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)

        # Trainorder data container
        statb_to_data_outer = wx.StaticBoxSizer(wx.StaticBox(self.pnl_to_right, wx.ID_ANY, u'Selected Trainorder'),
                                                wx.VERTICAL)
        # Trainorder data grid
        fgs_to_data_inner = wx.FlexGridSizer(0, 2, 0, 0)
        fgs_to_data_inner.SetFlexibleDirection(wx.BOTH)
        fgs_to_data_inner.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        # Trainorder ID
        self.lbl_to_id = wx.StaticText(statb_to_data_outer.GetStaticBox(), wx.ID_ANY, u'Train Order Record #:',
                                       wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_to_id.Wrap(-1)
        fgs_to_data_inner.Add(self.lbl_to_id, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.txt_to_id = wx.TextCtrl(statb_to_data_outer.GetStaticBox(), wx.ID_ANY, u'001', wx.DefaultPosition,
                                     wx.DefaultSize, wx.TE_READONLY)
        self.txt_to_id.SetMaxLength(4)
        self.txt_to_id.SetFont(
            wx.Font(wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD,
                    False, wx.EmptyString))
        self.txt_to_id.SetToolTip(u'Current trainorder ID')
        fgs_to_data_inner.Add(self.txt_to_id, 0, wx.ALL, 5)

        # Train order num
        self.lbl_to_num = wx.StaticText(statb_to_data_outer.GetStaticBox(), wx.ID_ANY, u'Train Order #:',
                                        wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_to_num.Wrap(-1)
        fgs_to_data_inner.Add(self.lbl_to_num, 0, wx.ALIGN_RIGHT | wx.ALL, 5)
        self.txt_to_num = wx.TextCtrl(statb_to_data_outer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                      wx.DefaultSize, 0)
        self.txt_to_num.SetToolTip(u' Train Order number recorded on trainorder slip')
        fgs_to_data_inner.Add(self.txt_to_num, 0, wx.ALIGN_LEFT | wx.ALL, 5)

        # Location
        self.lbl_loc = wx.StaticText(statb_to_data_outer.GetStaticBox(), wx.ID_ANY, u'Location Issued:',
                                     wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_loc.Wrap(-1)
        fgs_to_data_inner.Add(self.lbl_loc, 0, wx.ALIGN_RIGHT | wx.ALL, 5)
        self.txt_loc = wx.TextCtrl(statb_to_data_outer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                   wx.DefaultSize, 0)
        self.txt_loc.SetToolTip(u'Where the trainorder was issued')
        self.txt_loc.SetMinSize(wx.Size(300, -1))
        fgs_to_data_inner.Add(self.txt_loc, 0, wx.ALIGN_LEFT | wx.ALL, 5)

        # Date
        self.lbl_date = wx.StaticText(statb_to_data_outer.GetStaticBox(), wx.ID_ANY, u'Date:', wx.DefaultPosition,
                                      wx.DefaultSize, 0)
        self.lbl_date.Wrap(-1)
        fgs_to_data_inner.Add(self.lbl_date, 0, wx.ALIGN_RIGHT | wx.ALL, 5)
        self.dp_date = wx.adv.DatePickerCtrl(statb_to_data_outer.GetStaticBox(), wx.ID_ANY,
                                             wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize,
                                             wx.adv.DP_DEFAULT)
        fgs_to_data_inner.Add(self.dp_date, 0, wx.ALIGN_LEFT | wx.ALL, 5)

        # Train to whom the trainorder is issued
        self.lbl_to = wx.StaticText(statb_to_data_outer.GetStaticBox(), wx.ID_ANY, u'To Train:', wx.DefaultPosition,
                                    wx.DefaultSize, 0)
        self.lbl_to.Wrap(-1)
        fgs_to_data_inner.Add(self.lbl_to, 0, wx.ALIGN_RIGHT | wx.ALL, 5)
        self.txt_to = wx.TextCtrl(statb_to_data_outer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                  wx.DefaultSize, 0)
        self.txt_to.SetToolTip(u'Train to complete trainorder')
        self.txt_to.SetMinSize(wx.Size(300, -1))
        fgs_to_data_inner.Add(self.txt_to, 0, wx.ALIGN_LEFT | wx.ALL, 5)

        # At location
        self.lbl_at = wx.StaticText(statb_to_data_outer.GetStaticBox(), wx.ID_ANY, u'At:', wx.DefaultPosition,
                                    wx.DefaultSize, 0)
        self.lbl_at.Wrap(-1)
        fgs_to_data_inner.Add(self.lbl_at, 0, wx.ALIGN_RIGHT | wx.ALL, 5)
        self.txt_at = wx.TextCtrl(statb_to_data_outer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                  wx.DefaultSize, 0)
        self.txt_at.SetToolTip(u'Where the order is to occur')
        self.txt_at.SetMinSize(wx.Size(300, -1))
        fgs_to_data_inner.Add(self.txt_at, 0, wx.ALIGN_LEFT | wx.ALL, 5)

        # Message Text
        self.lbl_message = wx.StaticText(statb_to_data_outer.GetStaticBox(), wx.ID_ANY, u'Message Text:',
                                         wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_message.Wrap(-1)
        fgs_to_data_inner.Add(self.lbl_message, 0, wx.ALIGN_RIGHT | wx.ALL, 5)
        self.txt_message = wx.TextCtrl(statb_to_data_outer.GetStaticBox(), wx.ID_ANY, wx.EmptyString,
                                       wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL | wx.TE_MULTILINE)
        self.txt_message.SetToolTip(u'Oder details')
        self.txt_message.SetMinSize(wx.Size(300, 100))
        fgs_to_data_inner.Add(self.txt_message, 0, wx.ALIGN_LEFT | wx.ALL, 5)

        # Status
        self.lbl_status = wx.StaticText(statb_to_data_outer.GetStaticBox(), wx.ID_ANY, u'Status', wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.lbl_status.Wrap(-1)
        fgs_to_data_inner.Add(self.lbl_status, 0, wx.ALIGN_RIGHT | wx.ALL, 5)
        cb_status_choices = [u'Made Complete', u'Fulfilled', u'Superseded', u'Annulled']
        self.cb_status = wx.ComboBox(statb_to_data_outer.GetStaticBox(), wx.ID_ANY, u'Made Complete',
                                     wx.DefaultPosition, wx.DefaultSize, cb_status_choices, 0)
        self.cb_status.SetSelection(0)
        self.cb_status.SetToolTip(u'Trainorder status')
        fgs_to_data_inner.Add(self.cb_status, 0, wx.ALL, 5)

        # Time
        self.lbl_time = wx.StaticText(statb_to_data_outer.GetStaticBox(), wx.ID_ANY, u'Time:', wx.DefaultPosition,
                                      wx.DefaultSize, 0)
        self.lbl_time.Wrap(-1)
        fgs_to_data_inner.Add(self.lbl_time, 0, wx.ALIGN_RIGHT | wx.ALL, 5)
        self.tp_time = wx.adv.TimePickerCtrl(statb_to_data_outer.GetStaticBox(), wx.ID_ANY, style=wx.adv.TP_DEFAULT)
        self.tp_time.SetToolTip(u'Time trainorder was issued')
        fgs_to_data_inner.Add(self.tp_time, 0, wx.ALL, 5)

        # Dispatcher
        self.lbl_disp = wx.StaticText(statb_to_data_outer.GetStaticBox(), wx.ID_ANY, u'Dispatcher:', wx.DefaultPosition,
                                      wx.DefaultSize, 0)
        self.lbl_disp.Wrap(-1)
        fgs_to_data_inner.Add(self.lbl_disp, 0, wx.ALIGN_RIGHT | wx.ALL, 5)
        self.txt_disp = wx.TextCtrl(statb_to_data_outer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                    wx.DefaultSize, 0)
        self.txt_disp.SetToolTip(u'Name of dispatcher')
        self.txt_disp.SetMinSize(wx.Size(300, -1))
        fgs_to_data_inner.Add(self.txt_disp, 0, wx.ALIGN_LEFT | wx.ALL, 5)

        # Operator
        self.lbl_op = wx.StaticText(statb_to_data_outer.GetStaticBox(), wx.ID_ANY, u'Operator:', wx.DefaultPosition,
                                    wx.DefaultSize, 0)
        self.lbl_op.Wrap(-1)
        fgs_to_data_inner.Add(self.lbl_op, 0, wx.ALIGN_RIGHT | wx.ALL, 5)
        self.txt_op = wx.TextCtrl(statb_to_data_outer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                  wx.DefaultSize, 0)
        self.txt_op.SetToolTip(u'Name of morse operator')
        self.txt_op.SetMinSize(wx.Size(300, -1))
        fgs_to_data_inner.Add(self.txt_op, 0, wx.ALIGN_LEFT | wx.ALL, 5)

        # Station color
        self.lbl_station_color = wx.StaticText(statb_to_data_outer.GetStaticBox(), wx.ID_ANY, u'Station Color:',
                                               wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_station_color.Wrap(-1)
        fgs_to_data_inner.Add(self.lbl_station_color, 0, wx.ALL | wx.ALIGN_RIGHT, 5)
        cb_station_color_choices = [u'RED', u'GREEN', u'BLUE', u'CYAN', u'MAGENTA', u'YELLOW', u'WHITE']
        self.cb_station_color = wx.ComboBox(statb_to_data_outer.GetStaticBox(), wx.ID_ANY, u'WHITE', wx.DefaultPosition,
                                            wx.DefaultSize, cb_station_color_choices, 0)
        self.cb_station_color.SetToolTip(u'Color option for display during this trainorder')
        fgs_to_data_inner.Add(self.cb_station_color, 0, wx.ALL, 5)

        # Data layout End
        statb_to_data_outer.Add(fgs_to_data_inner, 1, wx.EXPAND, 5)

        # Data Panel Buttons
        bs_to_data_btns = wx.BoxSizer(wx.HORIZONTAL)
        self.btn_clear_to_data = wx.Button(statb_to_data_outer.GetStaticBox(), wx.ID_CLEAR, u'Clear',
                                           wx.DefaultPosition, wx.DefaultSize, 0)
        bs_to_data_btns.Add(self.btn_clear_to_data, 0, wx.ALL, 5)

        self.btn_undo_to_data = wx.Button(statb_to_data_outer.GetStaticBox(), wx.ID_UNDO, u'Undo All',
                                          wx.DefaultPosition, wx.DefaultSize, 0)
        self.btn_undo_to_data.SetToolTip(u'Undo changes')
        bs_to_data_btns.Add(self.btn_undo_to_data, 0, wx.ALL, 5)

        self.btn_save_to_data = wx.Button(statb_to_data_outer.GetStaticBox(), wx.ID_SAVE, u'Save', wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        self.btn_save_to_data.SetToolTip(u'Save changes')
        bs_to_data_btns.Add(self.btn_save_to_data, 0, wx.ALL, 5)
        # End Buttons

        statb_to_data_outer.Add(bs_to_data_btns, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.pnl_to_right.SetSizer(statb_to_data_outer)
        self.pnl_to_right.Layout()
        statb_to_data_outer.Fit(self.pnl_to_right)
        self.splitter_to.SplitVertically(self.pnl_to_left, self.pnl_to_right, 135)
        bs_to_outer.Add(self.splitter_to, 1, wx.EXPAND, 5)

        self.scrlwin_to.SetSizer(bs_to_outer)
        self.scrlwin_to.Layout()
        bs_to_outer.Fit(self.scrlwin_to)
        self.notebook.AddPage(self.scrlwin_to, u'Train Order', True)

        # Config Tab scroll Window
        self.scrlwin_conf = wx.ScrolledWindow(self.notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                              wx.HSCROLL | wx.VSCROLL)
        self.scrlwin_conf.SetScrollRate(5, 5)

        # Config outer container
        bs_conf_outer = wx.BoxSizer(wx.VERTICAL)

        # Morse config Box
        statb_morse = wx.StaticBoxSizer(wx.StaticBox(self.scrlwin_conf, wx.ID_ANY, u'Morse Speed'), wx.VERTICAL)

        fgs_morse_inner = wx.FlexGridSizer(2, 2, 0, 0)
        fgs_morse_inner.SetFlexibleDirection(wx.BOTH)
        fgs_morse_inner.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        cb_wpm_choices = [u'5', u'6', u'7', u'8', u'9', u'10', u'11', u'12', u'13', u'14', u'15', u'16', u'17', u'18',
                          u'19', u'20', u'21', u'22', u'23', u'24', u'25', u'26', u'27', u'28', u'29']
        self.cb_wpm = wx.ComboBox(statb_morse.GetStaticBox(), wx.ID_ANY, u'3', wx.DefaultPosition, wx.DefaultSize,
                                  cb_wpm_choices, wx.CB_READONLY)
        self.cb_wpm.SetSelection(0)
        fgs_morse_inner.Add(self.cb_wpm, 0, wx.ALL, 5)

        self.lbl_wpm = wx.StaticText(statb_morse.GetStaticBox(), wx.ID_ANY, u'Default Words per Minute',
                                     wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_wpm.Wrap(-1)
        fgs_morse_inner.Add(self.lbl_wpm, 0, wx.ALL, 5)

        cb_max_wpm_choices = [u'6', u'7', u'8', u'9', u'10', u'11', u'12', u'13', u'14', u'15', u'16', u'17', u'18',
                              u'19', u'20', u'21', u'22', u'23', u'24', u'25', u'26', u'27', u'28', u'29', u'30']
        self.cb_max_wpm = wx.ComboBox(statb_morse.GetStaticBox(), wx.ID_ANY, u'5', wx.DefaultPosition, wx.DefaultSize,
                                      cb_max_wpm_choices, wx.CB_READONLY)
        self.cb_max_wpm.SetSelection(0)
        fgs_morse_inner.Add(self.cb_max_wpm, 0, wx.ALL, 5)

        self.lbl_max_wpm = wx.StaticText(statb_morse.GetStaticBox(), wx.ID_ANY, u'Maximum Words per Minute',
                                         wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_max_wpm.Wrap(-1)
        fgs_morse_inner.Add(self.lbl_max_wpm, 0, wx.ALL, 5)

        statb_morse.Add(fgs_morse_inner, 1, wx.EXPAND, 5)

        bs_conf_outer.Add(statb_morse, 0, wx.ALL, 5)

        # PIN config Box
        statb_pin = wx.StaticBoxSizer(wx.StaticBox(self.scrlwin_conf, wx.ID_ANY, u'Pin Configuration'), wx.VERTICAL)

        radio_box_lcd_choices = [u'i2c Bus 0 (Pins 27, 28)', u'i2c Bus 1 (Pins 3, 5)']
        self.radio_box_lcd = wx.RadioBox(statb_pin.GetStaticBox(), wx.ID_ANY, u'LCD Bus (i2c)', wx.DefaultPosition,
                                         wx.DefaultSize, radio_box_lcd_choices, 1, wx.RA_SPECIFY_COLS)
        self.radio_box_lcd.SetSelection(0)
        statb_pin.Add(self.radio_box_lcd, 0, wx.ALL, 5)

        fgs_pin_inner = wx.FlexGridSizer(2, 2, 0, 0)
        fgs_pin_inner.SetFlexibleDirection(wx.BOTH)
        fgs_pin_inner.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        cb_relay_choices = [u'BCM 01 (28)', u'BCM 02 (03)', u'BCM 03 (05)', u'BCM 04 (07)', u'BCM 05 (29)',
                            u'BCM 06 (31)', u'BCM 07 (26)', u'BCM 08 (24)', u'BCM 09 (21)', u'BCM 10 (19)',
                            u'BCM 11 (23)', u'BCM 12 (32)', u'BCM 13 (33)', u'BCM 14 (08)', u'BCM 15 (10)',
                            u'BCM 16 (36)', u'BCM 17 (11)', u'BCM 18 (12)', u'BCM 19 (35)', u'BCM 20 (38)',
                            u'BCM 21 (40)', u'BCM 22 (15)', u'BCM 23 (16)', u'BCM 24 (18)', u'BCM 25 (22)',
                            u'BCM 26 (37)', u'BCM 27 (13)']
        self.cb_relay = wx.ComboBox(statb_pin.GetStaticBox(), wx.ID_ANY, u'BCM 01 (28)', wx.DefaultPosition,
                                    wx.DefaultSize, cb_relay_choices, wx.CB_READONLY)
        self.cb_relay.SetSelection(0)
        fgs_pin_inner.Add(self.cb_relay, 0, wx.ALL, 5)

        self.lbl_relay = wx.StaticText(statb_pin.GetStaticBox(), wx.ID_ANY, u'Relay Pin', wx.DefaultPosition,
                                       wx.DefaultSize, 0)
        self.lbl_relay.Wrap(-1)
        fgs_pin_inner.Add(self.lbl_relay, 0, wx.ALL, 5)

        cb_pir_choices = [u'BCM 01 (28)', u'BCM 02 (03)', u'BCM 03 (05)', u'BCM 04 (07)', u'BCM 05 (29)',
                          u'BCM 06 (31)', u'BCM 07 (26)', u'BCM 08 (24)', u'BCM 09 (21)', u'BCM 10 (19)',
                          u'BCM 11 (23)', u'BCM 12 (32)', u'BCM 13 (33)', u'BCM 14 (08)', u'BCM 15 (10)',
                          u'BCM 16 (36)', u'BCM 17 (11)', u'BCM 18 (12)', u'BCM 19 (35)', u'BCM 20 (38)',
                          u'BCM 21 (40)', u'BCM 22 (15)', u'BCM 23 (16)', u'BCM 24 (18)', u'BCM 25 (22)',
                          u'BCM 26 (37)', u'BCM 27 (13)']
        self.cb_pir = wx.ComboBox(statb_pin.GetStaticBox(), wx.ID_ANY, u'BCM 02 (03)', wx.DefaultPosition,
                                  wx.DefaultSize, cb_pir_choices, wx.CB_READONLY)
        self.cb_pir.SetSelection(1)
        fgs_pin_inner.Add(self.cb_pir, 0, wx.ALL, 5)
        self.lbl_pir = wx.StaticText(statb_pin.GetStaticBox(), wx.ID_ANY, u'PIR Motion Detector Pin',
                                     wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_pir.Wrap(-1)
        fgs_pin_inner.Add(self.lbl_pir, 0, wx.ALL, 5)

        statb_pin.Add(fgs_pin_inner, 0, 0, 5)

        bs_conf_outer.Add(statb_pin, 0, wx.ALL, 5)

        # General Config
        statb_gen = wx.StaticBoxSizer(wx.StaticBox(self.scrlwin_conf, wx.ID_ANY, 'General Options'), wx.VERTICAL)

        fgs_gen_inner = wx.FlexGridSizer(3, 2, 0, 0)
        fgs_gen_inner.SetFlexibleDirection(wx.BOTH)
        fgs_gen_inner.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.chkb_speed = wx.CheckBox(statb_gen.GetStaticBox(), wx.ID_ANY, u'Enabled', wx.DefaultPosition,
                                      wx.DefaultSize, 0)
        fgs_gen_inner.Add(self.chkb_speed, 0, wx.ALL, 5)
        self.lbl_speed = wx.StaticText(statb_gen.GetStaticBox(), wx.ID_ANY,
                                       u'Speed Adjust using Left and Right Buttons on LCD Plate', wx.DefaultPosition,
                                       wx.DefaultSize, 0)
        self.lbl_speed.Wrap(-1)
        fgs_gen_inner.Add(self.lbl_speed, 0, wx.ALL, 5)

        cb_color_choices = [u'RED', u'GREEN', u'BLUE', u'CYAN', u'MAGENTA', u'YELLOW', u'WHITE']
        self.cb_color = wx.ComboBox(statb_gen.GetStaticBox(), wx.ID_ANY, u'Red', wx.DefaultPosition, wx.DefaultSize,
                                    cb_color_choices, wx.CB_READONLY)
        self.cb_color.SetSelection(0)
        fgs_gen_inner.Add(self.cb_color, 0, wx.ALL, 5)
        self.lbl_color = wx.StaticText(statb_gen.GetStaticBox(), wx.ID_ANY, u'LCD Display Color', wx.DefaultPosition,
                                       wx.DefaultSize, 0)
        self.lbl_color.Wrap(-1)
        fgs_gen_inner.Add(self.lbl_color, 0, wx.ALL, 5)

        self.txt_paragraph_sep = wx.TextCtrl(statb_gen.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        fgs_gen_inner.Add(self.txt_paragraph_sep, 0, wx.ALL, 5)
        self.lbl_paragraph_sep = wx.StaticText(statb_gen.GetStaticBox(), wx.ID_ANY,
                                               u'Paragraph separator shown on LCD during display', wx.DefaultPosition,
                                               wx.DefaultSize, 0)
        self.lbl_paragraph_sep.Wrap(-1)
        fgs_gen_inner.Add(self.lbl_paragraph_sep, 0, wx.ALL, 5)

        statb_gen.Add(fgs_gen_inner, 0, 0, 5)
        bs_conf_outer.Add(statb_gen, 1, wx.ALL, 5)

        self.scrlwin_conf.SetSizer(bs_conf_outer)
        self.scrlwin_conf.Layout()
        bs_conf_outer.Fit(self.scrlwin_conf)
        self.notebook.AddPage(self.scrlwin_conf, u'Configuration', False)

        bs_main.Add(self.notebook, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bs_main)
        self.Layout()

        self.menubar = wx.MenuBar(0)
        # ----------------------------
        self.menu_file = wx.Menu()
        self.menuitem_new_to = wx.MenuItem(self.menu_file, wx.ID_ANY, u'&New Trainorder File' + u'\t' + u'Ctrl-N',
                                           wx.EmptyString, wx.ITEM_NORMAL)
        self.menu_file.Append(self.menuitem_new_to)
        self.menuitem_new_conf = wx.MenuItem(self.menu_file, wx.ID_ANY, u'N&ew Config File' + u'\t' + u'Ctrl-E',
                                             wx.EmptyString, wx.ITEM_NORMAL)
        self.menu_file.Append(self.menuitem_new_conf)
        self.menu_file.AppendSeparator()
        self.menuitem_open_to = wx.MenuItem(self.menu_file, wx.ID_ANY, u'&Open Trainorder File...' + u'\t' + u'Ctrl-O',
                                            wx.EmptyString, wx.ITEM_NORMAL)
        self.menu_file.Append(self.menuitem_open_to)
        self.menuitem_open_conf = wx.MenuItem(self.menu_file, wx.ID_ANY, u'Open Config File...' + u'\t' + u'Ctrl-F',
                                              wx.EmptyString, wx.ITEM_NORMAL)
        self.menu_file.Append(self.menuitem_open_conf)
        self.menu_file.AppendSeparator()
        self.menuitem_save_to = wx.MenuItem(self.menu_file, wx.ID_ANY, u'Save Trainorder File', wx.EmptyString,
                                            wx.ITEM_NORMAL)
        self.menu_file.Append(self.menuitem_save_to)
        self.menuitem_save_conf = wx.MenuItem(self.menu_file, wx.ID_ANY, u'Save Config File', wx.EmptyString,
                                              wx.ITEM_NORMAL)
        self.menu_file.Append(self.menuitem_save_conf)
        self.menuitem_save_all = wx.MenuItem(self.menu_file, wx.ID_SAVE, u'Save All', wx.EmptyString, wx.ITEM_NORMAL)
        self.menu_file.Append(self.menuitem_save_all)
        self.menu_file.AppendSeparator()
        self.menuitem_save_to_as = wx.MenuItem(self.menu_file, wx.ID_ANY, u'Save Trainorder File As...',
                                               wx.EmptyString, wx.ITEM_NORMAL)
        self.menu_file.Append(self.menuitem_save_to_as)
        self.menuitem_save_conf_as = wx.MenuItem(self.menu_file, wx.ID_ANY, u'Save Config File As...',
                                                 wx.EmptyString, wx.ITEM_NORMAL)
        self.menu_file.Append(self.menuitem_save_conf_as)
        self.menu_file.AppendSeparator()
        self.menuitem_exit = wx.MenuItem(self.menu_file, wx.ID_EXIT, u'&Quit' + u'\t' + u'Alt-F4', wx.EmptyString,
                                         wx.ITEM_NORMAL)
        self.menu_file.Append(self.menuitem_exit)
        self.menubar.Append(self.menu_file, u'&File')

        # ----------------------------
        self.menu_edit = wx.Menu()
        self.menuitem_undo = wx.MenuItem(self.menu_edit, wx.ID_UNDO, u'Undo' + u'\t' + u'Ctrl-Z', wx.EmptyString,
                                         wx.ITEM_NORMAL)
        self.menu_edit.Append(self.menuitem_undo)
        self.menuitem_redo = wx.MenuItem(self.menu_edit, wx.ID_REDO, u'Redo' + u'\t' + u'Ctrl-Q', wx.EmptyString,
                                         wx.ITEM_NORMAL)
        self.menu_edit.Append(self.menuitem_redo)
        self.menu_edit.AppendSeparator()
        self.menuitem_cut = wx.MenuItem(self.menu_edit, wx.ID_CUT, u'Cut' + u'\t' + u'Ctrl-X', wx.EmptyString,
                                        wx.ITEM_NORMAL)
        self.menu_edit.Append(self.menuitem_cut)
        self.menuitem_copy = wx.MenuItem(self.menu_edit, wx.ID_COPY, u'Copy' + u'\t' + u'Ctrl-C', wx.EmptyString,
                                         wx.ITEM_NORMAL)
        self.menu_edit.Append(self.menuitem_copy)
        self.menuitem_paste = wx.MenuItem(self.menu_edit, wx.ID_PASTE, u'Paste' + u'\t' + u'Ctrl-P', wx.EmptyString,
                                          wx.ITEM_NORMAL)
        self.menu_edit.Append(self.menuitem_paste)
        self.menubar.Append(self.menu_edit, u'&Edit')

        # ----------------------------
        self.about = wx.Menu()
        self.menuitem_about = wx.MenuItem(self.about, wx.ID_ABOUT, u'About', wx.EmptyString, wx.ITEM_NORMAL)
        self.about.Append(self.menuitem_about)
        self.menubar.Append(self.about, u'&About')

        # ----------------------------
        self.SetMenuBar(self.menubar)

        self.status_bar = self.CreateStatusBar(1, wx.STB_SIZEGRIP, wx.ID_ANY)
        self.Center(wx.BOTH)

        # Connect Events
        self.notebook.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.functions.on_notebook_tab_change)
        self.btn_add_to.Bind(wx.EVT_BUTTON, self.functions.on_btn_add_to)
        self.btn_delete_to.Bind(wx.EVT_BUTTON, self.functions.on_btn_delete_to)
        self.btn_clear_to_data.Bind(wx.EVT_BUTTON, self.functions.on_btn_clear_to_data)
        self.btn_undo_to_data.Bind(wx.EVT_BUTTON, self.functions.on_btn_undo_to_data)
        self.btn_save_to_data.Bind(wx.EVT_BUTTON, self.functions.on_btn_save_to_data)
        self.cb_wpm.Bind(wx.EVT_ENTER_WINDOW, self.functions.wpm_update)
        self.cb_wpm.Bind(wx.EVT_KILL_FOCUS, self.functions.wpm_update)
        self.cb_wpm.Bind(wx.EVT_LEAVE_WINDOW, self.functions.wpm_update)
        self.cb_wpm.Bind(wx.EVT_SET_FOCUS, self.functions.wpm_update)
        self.Bind(wx.EVT_MENU, self.functions.on_menuitem_new_to, id=self.menuitem_new_to.GetId())
        self.Bind(wx.EVT_MENU, self.functions.on_menuitme_new_conf, id=self.menuitem_new_conf.GetId())
        self.Bind(wx.EVT_MENU, self.functions.on_menuitem_open_to, id=self.menuitem_open_to.GetId())
        self.Bind(wx.EVT_MENU, self.functions.on_menuitem_open_conf, id=self.menuitem_open_conf.GetId())
        self.Bind(wx.EVT_MENU, self.functions.on_menuitem_save_to, id=self.menuitem_save_to.GetId())
        self.Bind(wx.EVT_MENU, self.functions.on_menuitem_save_conf, id=self.menuitem_save_conf.GetId())
        self.Bind(wx.EVT_MENU, self.functions.on_menuitem_save_all, id=self.menuitem_save_all.GetId())
        self.Bind(wx.EVT_MENU, self.functions.on_menuitem_save_to_as, id=self.menuitem_save_to_as.GetId())
        self.Bind(wx.EVT_MENU, self.functions.on_menuitem_save_conf_as, id=self.menuitem_save_conf_as.GetId())
        self.Bind(wx.EVT_MENU, self.functions.on_menuitem_exit, id=self.menuitem_exit.GetId())
        self.Bind(wx.EVT_MENU, self.functions.on_menuitem_undo, id=self.menuitem_undo.GetId())
        self.Bind(wx.EVT_MENU, self.functions.on_menuitem_redo, id=self.menuitem_redo.GetId())
        self.Bind(wx.EVT_MENU, self.functions.on_menuitem_cut, id=self.menuitem_cut.GetId())
        self.Bind(wx.EVT_MENU, self.functions.on_menuitem_copy, id=self.menuitem_copy.GetId())
        self.Bind(wx.EVT_MENU, self.functions.on_menuitem_paste, id=self.menuitem_paste.GetId())
        self.Bind(wx.EVT_MENU, self.functions.on_menuitem_about, id=self.menuitem_about.GetId())

        def __del__(self):
            pass
