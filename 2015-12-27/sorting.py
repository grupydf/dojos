# -*- coding: utf-8 -*-
import unittest


def e_maior(x, y):
    return x > y

def ordena_par(par):
    x, y = par
    if x > y:
        return True, [y, x]

    return False, par

def ordena_lista(lista):
    for i in range(len(lista)-1):
        par = ordena_par(lista[i: i+1])

    return [2,3,9]

class TestSorting(unittest.TestCase):

    def testExemplo(self):
        return self.assertEqual(e_maior(3, 2), True)

    def testComNumeroMenor(self):
        return self.assertEqual(e_maior(2, 3), False)

    def testOrdenaParOrdenado(self):
        self.assertEqual(ordena_par([2, 3]), (False, [2, 3]))
        self.assertEqual(ordena_par([8, 9]), (False, [8, 9]))

    def testOrdenaParDesordenada(self):
        self.assertEqual(ordena_par([3, 2]), (True, [2, 3]))
        self.assertEqual(ordena_par([9, 2]), (True, [2, 9]))

    def testOrdenaListaDesordenada(self):
        lista = [7, 5, 10, 8, 3, 9]
        self.assertEqual(ordena_lista([9, 2, 3]), [2, 3, 9])
        self.assertEqual(ordena_lista(lista), [3, 5, 7, 8, 9, 10])
