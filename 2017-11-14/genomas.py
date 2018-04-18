#!/usr/bin/env python
"""

>>> calcula_genoma('A')
'A 1'

>>> calcula_genoma('AA')
'A 2'

>>> calcula_genoma('AAA')
'A 3'

>>> calcula_genoma('AC')
'A 1 C 1'

>>> calcula_genoma('ACCG')
'A 1 C 2 G 1'

>>> calcula_genoma('ACCGTT')
'A 1 C 2 G 1 T 2'

>>> calcula_genoma('')
''

>>> calcula_genoma('CCCGTT')
'C 3 G 1 T 2'
>>> calcula_genoma('GTT')
'G 1 T 2'
>>> calcula_genoma('TT')
'T 2'
>>> calcula_genoma('ACTTTTTGGGGGGGGGTT')
'A 1 C 1 G 9 T 7'
"""

import doctest


def calcula_genoma(genoma):
    resultado = ''

    adenosina = genoma.count('A')
    citosina = genoma.count('C')
    guanina = genoma.count('G')
    tinina = genoma.count('T')

    if adenosina != 0:
        resultado += f'A {adenosina}'

    if citosina != 0:
        if resultado:
            resultado += ' '
        resultado += f'C {citosina}'

    if guanina != 0:
        if resultado:
            resultado += ' '
        resultado += f'G {guanina}'

    if tinina != 0:
        if resultado:
            resultado += ' '
        resultado += f'T {tinina}'

    return resultado


if __name__ == '__main__':
    doctest.testmod(verbose=True)
