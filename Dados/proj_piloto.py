# Calculadora

import math as mt

def somatorio2(x, i):
    lista = []
    while i <= x:
        sm = i
        lista.append(sm)
        i += 1
    sm = sum(lista)
    return sm

print('-'*22)
print('| Calculadora básica |')
print('-'*22)

n = input('Escolha a operação:\n1 - Somatório\n2 - Eq.2° Grau\n3 - Multiplicação de matrizes\n--->  ')
if n == 1:
    i = input('Somatório de: ')
    x = input('Até: ')
    somat = somatorio2(x,i)
print(somat)
   
    
