# coding=utf-8
"""
CERMMorse : test_workOrder
5/7/2017 : 11:34 PM
Author : James L. Key
"""
from random import randrange
from unittest import TestCase

from workorder import WorkOrder

__author__ = 'James L. Key'
__project__ = 'CERMMorse'


class TestWorkOrder(TestCase):
    def setUp(self):
        self.wo = WorkOrder(wopath='../data/work_orders.json')

    def test_getworkorder(self):
        self.wo.getworkorder(randrange(1, self.wo.numworkorders()))
        self.assertIsInstance(self.wo.TONum, str)
        self.assertIsInstance(self.wo.LocIssued, str)
        self.assertIsInstance(self.wo.Date, str)
        self.assertIsInstance(self.wo.To, str)
        self.assertIsInstance(self.wo.At, str)
        self.assertIsInstance(self.wo.Text, str)
        self.assertIsInstance(self.wo.Status, str)
        self.assertIsInstance(self.wo.Time, str)
        self.assertIsInstance(self.wo.Dispatcher, str)
        self.assertIsInstance(self.wo.Operator, str)

    def test_numworkorders(self):
        #  This Test is pathetic, it check only if the returned number is a positive integer
        wonum = self.wo.numworkorders()
        self.assertIsInstance(wonum, int, 'Number of Work Orders is not an Integer!!')
        self.assertGreaterEqual(wonum, 1, 'Number of Work Orders is less than 1!!')
