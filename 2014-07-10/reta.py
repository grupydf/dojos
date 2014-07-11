#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

def is_vertical(reta):
    p1, p2 = reta
    x1, y1 = p1
    x2, y2 = p2
    return bool(x1 == x2)

def angulo(reta):
    p1, p2 = reta
    x1, y1 = p1
    x2, y2 = p2
    return abs(y2 - y1) / abs(x2 - x1)

def possui_intersecao(r1, r2):
    if is_vertical(r1) and is_vertical(r2):
        return False

    m1 = angulo(r1)
    m2 = angulo(r2)

    if m1 == m2:
        return False

    return True


class TestSomething(unittest.TestCase):
    diagonal1 = ((1, 1), (3, 3))
    diagonal2 = ((2, 1), (4, 3))

    horizontal1 = ((1, 4), (3, 4))
    horizontal2 = ((1, 5), (3, 5))

    vertical1 = ((6, 1), (6, 3))
    vertical2 = ((7, 1), (7, 3))

    def testPossuiIntersecao(self):
        self.assertTrue(
            possui_intersecao(
                self.diagonal1,
                self.horizontal1,
                ))

    def testNaoPossuiIntersecaoHorizontal(self):
        self.assertFalse(
            possui_intersecao(
                self.horizontal1,
                self.horizontal2,
                ))

    def testNaoPossuiIntersecaoVertical(self):
        self.assertFalse(
            possui_intersecao(
                self.vertical1,
                self.vertical2,
                ))

    def testNaoPossuiIntersecaoDiagonal(self):
        self.assertFalse(
            possui_intersecao(
                self.diagonal1,
                self.diagonal2,
                ))

