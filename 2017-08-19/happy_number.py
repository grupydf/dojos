#!/Users/juliosaraiva/Documents/dojo/app/bin/python3
# Link do problema: http://dojopuzzles.com/problemas/exibe/numeros-felizes/
def happy_number(num):

    if num < 10:
        return num == 1 or num == 7
    else:
        return happy_number(soma_quadrado(num))

def soma_quadrado(n):

# Testes
assert happy_number(2890) == False
assert happy_number(3) == False
assert soma_quadrado(7) == 49
assert soma_quadrado(49) == 97
assert soma_quadrado(97) == 130
assert soma_quadrado(130) == 10
assert soma_quadrado(10) == 1
assert happy_number(4) == False
assert happy_number(9) == False
assert happy_number(2) == False
assert happy_number(97) == True
assert happy_number(130) == True
assert happy_number(64) == False
assert happy_number(25) == False
