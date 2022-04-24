from random import choice

l = []

for i in range(5):
    n = input('Digite um nome: ')
    l.append(n)
    
sorteio = choice(l)
print('A pessoa sorteada foi {}, parabéns!!'.format(sorteio))
