#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

'''
    Definição da Torre de Hanoi
    ([3, 2, 1], [], [])
'''


def hanoi_num_movimentos(n):
    """n = numero de aneis
    retorno: numero de passos necessarios pra resolver o prob
    """
    return 2 ** n - 1


def hanoi_valida_posicao(lista):
    """lista = ordem dos blocos
    """
    return lista == list(reversed(sorted(lista)))


def hanoi_cria_torre(n):
    return (list(reversed(range(n))), [], [])


def hanoi_valida_estado(estado):
    if not isinstance(estado, (tuple, list)) or \
       not isinstance(estado[0], (tuple, list)):
        return False

    if not len(estado) == 3:
        return False

    for torre in (estado):
        if not hanoi_valida_posicao(torre):
            return False

    # lista contendo todos os elementos de todas as torres
    todas_as_torres = estado[0] + estado[1] + estado[2]

    if len(todas_as_torres) != len(set(todas_as_torres)):
        return False

    return True


class TestSomething(unittest.TestCase):
    def test_hanoi_sem_anel(self):
        # para um anel, e necessaria uma interacao pra resolver prob
        self.assertEqual(0, hanoi_num_movimentos(0))

    def test_hanoi_um_anel(self):
        self.assertEqual(1, hanoi_num_movimentos(1))

    def test_posicao_valida(self):
        self.assertTrue(hanoi_valida_posicao([3, 2, 1]))

    def test_posicao_invalida(self):
        self.assertFalse(hanoi_valida_posicao([1, 2, 3]))

    def test_criacao_torre(self):
        self.assertEqual(([2, 1, 0], [], []), hanoi_cria_torre(3))

    def test_estado_correto(self):
        self.assertTrue(hanoi_valida_estado(([2, 1, 0], [], [])))

    def test_estado_fora_de_ordem(self):
        self.assertFalse(hanoi_valida_estado(([0, 2, 1], [], [])))

    def test_estado_com_mais_ou_menos_torres(self):
        self.assertFalse(hanoi_valida_estado(([2, 1, 0])))
        self.assertFalse(hanoi_valida_estado(([2, 1, 0],)))
        self.assertFalse(hanoi_valida_estado(([2, 1, 0], [], [], [])))

    def test_estado_repeticao(self):
        self.assertFalse(hanoi_valida_estado(([2, 1, 0], [0], [])))
