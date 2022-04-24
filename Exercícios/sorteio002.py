# SORTEI DE UM JOGO ENTRE 2 CLUBES

from random import choice

times = []

for i in range(4):
    t = input('Time: ')
    times.append(t)

sorteio1 = choice(times)
sorteio2 = choice(times)
if sorteio1 == sorteio2:
    sorteio1 = choice(times)
    sorteio2 = choice(times)
else:
    print('\033[1;30;44m {} X {} \033[m'.format(sorteio1, sorteio2))
