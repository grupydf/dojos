# -*- coding: utf-8 -*-

import unittest

matrix = [[0, 0, 0],
          [0, 1, 0],
          [0, 0, 1]]

matrix2 = [[0, 0, 0],
          [0, 0, 1],
          [1, 0, 1]]

matrix3 = [[0, 0, 1],
          [0, 1, 1],
          [1, 0, 1]]

matrix4 = [[0, 0, 0],
           [0, 1, 1],
           [1, 0, 1]]

matrix5 = [[0, 0, 0],
           [0, 1, 0],
           [0, 0, 0]]

def regra1(matrix):
    if soma_matrix(matrix) < 2:
        return 0

def regra2(matrix):
    if soma_matrix(matrix) > 3:
        return 0
def regra3(matrix):
    return 1 if soma_matrix(matrix) == 3 else 0 


def soma_matrix(matrix):
    resultado = -1*matrix[1][1]
    for line in matrix:
        resultado += sum(line)
    return resultado

class TestGameOfLife(unittest.TestCase):

    def testRegra1_menos_de_dois_morre(self):
        return self.assertEqual(regra1(matrix), 0)

    def testRegra2_mais_de_tres_morre(self):
        return self.assertEqual(regra2(matrix3), 0)

    def testRegra3_igual_a_tres_vive(self):
        return self.assertEqual(regra3(matrix2), 1)

    def testRegra3_igual_a_tres_vive_com_meio_vivo(self):
        return self.assertEqual(regra3(matrix4), 1)    

        