#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest


def something():
    return True


class TestSomething(unittest.TestCase):
    def testSomething(self):
        self.assertTrue(something())
