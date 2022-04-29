# PROGRAMA CALCULA O SOMATÓRIO E FATORIAL DE UM NÚMERO

def fatorial(x):
    if x == 1:
        return 1
    else:
        return x * fatorial(x - 1)


def somatorio2(x, i):
    lista = []
    while i <= x:
        sm = i
        lista.append(sm)
        i += 1
    sm = sum(lista)
    return sm


teste1 = somatorio2(5, 1)
print(teste1)
