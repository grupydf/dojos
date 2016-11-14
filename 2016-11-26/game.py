# -*- coding: utf-8 -*-

import unittest


def exemplo():
    return True


class TestGameOfLife(unittest.TestCase):

    def testExemplo(self):
        return self.assertTrue(exemplo())
