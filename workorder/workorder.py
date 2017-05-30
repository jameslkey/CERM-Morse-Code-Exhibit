# coding=utf-8
"""
CERMMorse : workorder
5/12/2017 : 3:46 PM
Author : James L. Key

-- Frozen JSON is borrowed from  “Fluent Python by Luciano Ramalho (O’Reilly).
-- Copyright 2015 Luciano Ramalho, 978-1-491-94600-8.”
"""
# todo: add more comments
import codecs
import json
import os

try:
    from frozenjson import FrozenJSON
except ImportError:
    import sys

    FrozenJSON = sys.modules[__package__ + '.FrozenJSON']

__author__ = 'James L. Key'
__project__ = 'CERMMorse'


class WorkOrder:
    def __init__(self, wopath=''):

        if wopath == '':
            wopath = os.path.dirname(os.getcwd())
            wopath = os.path.join(wopath, 'CERMMorse')
            wopath = os.path.join(wopath, 'data')
            wopath = os.path.join(wopath, 'work_orders.json')
        j_s_o_n = os.path.normpath(wopath)
        if not os.path.exists(j_s_o_n):
            raise WorkOrderEx('Work Order File {} does not exists'.format(j_s_o_n))
        with codecs.open(j_s_o_n, 'r', encoding='utf-8') as f:  # Needs encoding to force raspbian to read correctly
            self._rawwodata = json.load(f)
        self._wodata = FrozenJSON(self._rawwodata)
        self.TONum = 0
        self.LocIssued = ''
        self.Date = ''
        self.To = ''
        self.At = ''
        self.Text = ''
        self.Status = 0
        self.Time = 0
        self.Dispatcher = ''
        self.Operator = ''

    def getworkorder(self, woid=1):
        if woid <= 0:
            raise WorkOrderEx('Work Order Number must be Greater than zero')
        if woid > self.numworkorders():
            raise WorkOrderEx('Work Order Does not exist in file or file is improperly formatted')
        woid = woid - 1
        self.TONum = str(self._wodata.WorkOrder[woid].TONum)
        self.LocIssued = str(self._wodata.WorkOrder[woid].LocIssued)
        self.Date = str(self._wodata.WorkOrder[woid].Date)
        self.To = str(self._wodata.WorkOrder[woid].To)
        self.At = str(self._wodata.WorkOrder[woid].At)
        self.Text = str(self._wodata.WorkOrder[woid].Text)
        self.Status = str(self._wodata.WorkOrder[woid].Status)
        self.Time = str(self._wodata.WorkOrder[woid].Time)
        self.Dispatcher = str(self._wodata.WorkOrder[woid].Dispatcher)
        self.Operator = str(self._wodata.WorkOrder[woid].Operator)

    def numworkorders(self):
        wos = 0
        for _ in self._rawwodata['WorkOrder']:
            wos = wos + 1
        return wos


class WorkOrderEx(Exception):
    def __init__(self, message):
        self.message = message
