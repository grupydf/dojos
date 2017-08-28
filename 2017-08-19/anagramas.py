#!/Users/juliosaraiva/Documents/dojo/app/bin/python3
# Link do problema: http://dojopuzzles.com/problemas/exibe/anagramas/

def permute(inp):
    tam = len(inp)
    if tam < 2:
        return {inp}
    if tam == 2:
        return {inp, inp[1] + inp[0]}
    else:
        resultado = set()
        for i in range(tam):
            # pega inp sem a i-ésima letra
            palavra = inp[:i]+ inp[i+1:]
            for permutation in permute(palavra):
                resultado.add(inp[i] + permutation)
        return resultado

#test
assert permute('') == {''}
assert permute('a') == {'a'}
assert permute('b') == {'b'}
assert permute('ab') == {'ab', 'ba'}
assert permute('ab') == {'ba', 'ab'}
assert permute('xy') == {'xy', 'yx'}
assert permute('abc') == {'abc', 'acb',
                          'bac', 'bca',
                          'cab', 'cba'}
assert len(permute('xyz')) == 6
assert len(permute('abcd')) == 24
assert permute('abcd') == {'bdac', 'cadb', 'adbc',
                           'adcb', 'acdb', 'abdc',
                           'cbad', 'acbd', 'dabc',
                           'dbca', 'cabd', 'bcda',
                           'cdab', 'cbda', 'dacb',
                           'dcab', 'bcad', 'dbac',
                           'bdca', 'abcd', 'bacd',
                           'badc', 'cdba', 'dcba'}
assert permute('biro') == {'biro', 'bior', 'brio',
                           'broi', 'boir', 'bori',
                           'ibro', 'ibor', 'irbo',
                           'irob', 'iobr', 'iorb',
                           'rbio', 'rboi', 'ribo',
                           'riob', 'roib', 'robi',
                           'obir', 'obri', 'oibr',
                           'oirb', 'orbi', 'orib'}
