# coding utf-8
import string

def shift(char):
    alfabeto = list(string.ascii_lowercase)
    alfabeto.append(' ')
    index = alfabeto.index(char)
    index = (index + 3) % 27
    return alfabeto[index]

def cesar(string):
    cifra = ''
    for char in string:
        cifra = cifra + shift(char)

    return cifra

def test_shift_a_d():
    assert shift('a') == 'd'

def test_shift_b_e():
    assert shift('b') == 'e'

def test_shift_e_h():
    assert shift('e') == 'h' 

def test_shift_x__():
    assert shift('x') == ' '  

def test_shift_y_a():
    assert shift('y') == 'a'

def test_cesar():
    assert cesar('ma') == 'pd'

def test_cesar_2():
    assert cesar('pe') == 'sh'

def test_freak_message():
    assert cesar('dojo iesb') == 'grmrclhve'