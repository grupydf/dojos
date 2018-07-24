"""
diamante('c')
   a
  b b
 c   c
  b b
   a
 """

listaTemp = []
abcedario = ['a', 'b', 'c', 'd', ]
alfabeto = 'abcdefghijklmnopqrstuvwxyz'

j = 0
lista2 = []
k = 0


def sequencia(letra):
    index = alfabeto.find(letra)

    lista = list(alfabeto[:index])

    return lista + [letra] + lista[::-1]


"""
    for i in alfabeto:
            if letra != i:
                     listaTemp.append(i)
            else:
                    listaTemp.append(i)
                    break
    j=len(listaTemp)
    j = j-1
    lista2 = listaTemp.copy()
    while j > k :
            lista2.append(listaTemp[j-1])
            j = j - 1

    return lista2
"""


def test_sequence_a():
    assert sequencia('a') == ['a']


def test_sequence_b():
    assert sequencia('b') == ['a', 'b', 'a']


def test_sequence_c():
    assert sequencia('c') == ['a', 'b', 'c', 'b', 'a']
