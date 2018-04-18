#!/usr/bin/env python
"""
# Ouro (D), Copa (H), Espadas (S), Paus (C)
# 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A

#    Carta Alta: A carta de maior valor.
#    Um Par: Duas cartas do mesmo valor.
#    Dois Pares: Dois pares diferentes.
#    Trinca: Três cartas do mesmo valor e duas de valores diferentes.
#    Straight (seqüência): Todas as carta com valores consecutivos.
#    Flush: Todas as cartas do mesmo naipe.
#    Full House: Um trinca e um par.
#    Quadra: Quatro cartas do mesmo valor.
#    Straight Flush: Todas as cartas são consecutivas e do mesmo naipe.
#    Royal Flush: A seqüência 10, Valete, Dama, Rei, Ás, do mesmo naipe.

# poker(['2H', '3D', '4S', '6C', '10C'], ['AD', 'AH', 'AS', '2H', '2D'])
# 2

>>> poker(1, 2)
Traceback (most recent call last):
	...
Exception: Entre com duas listas

>>> poker([], 2)
Traceback (most recent call last):
	...
Exception: Entre com duas listas

>>> poker(['2H', '3D', '4S', '6C'], [])
Traceback (most recent call last):
	...
Exception: O Array precisa conter 5

>>> poker(['2H', '3D', '4S', '6C', '7D'], ['2H', '3D', '4S', '6C'])
Traceback (most recent call last):
	...
Exception: O Array precisa conter 5

>>> naipe('2H')
'H'

>>> valor('2H')
'2'

>>> valor('10S')
'10'

>>> flush(['2H', '3H', '4H', '6H', '7H'])
True

>>> flush(['2S', '3H', '4H', '6H', '7H'])
False

>>> dupla(['2S', '3H', '4H', '6H', '7H'])
False

 
"""

['2H', '3']

import doctest

	
def dupla(jogador):
	numero = valor(jogador[0])
	for carta in jogador:
		if numero != numero(carta):
			return False
	return True

def flush(jogador):
	letra = naipe(jogador[0])
	for carta in jogador:
		if letra != naipe(carta):
			return False
	return True

def valor(carta):
	valor = carta[:-1]
	return valor


def naipe(carta):
	return carta[-1]



def poker(jogador1, jogador2):
	if type(jogador1) is not list:
		raise Exception('Entre com duas listas')
	if type(jogador2) is not list:
		raise Exception('Entre com duas listas')

	if len(jogador1) != 5:
		raise Exception('O Array precisa conter 5')
	if len(jogador2) != 5:
		raise Exception('O Array precisa conter 5')


	return False


if __name__ == '__main__':
    doctest.testmod(verbose=False)
