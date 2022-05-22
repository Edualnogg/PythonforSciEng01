print('-'*25)
print('----> | TABUADA | <----')
print('-'*25)

n = int(input('Digite um número:'))
print('-'*20)
for i in range(11):
    multipli = (n*i)
    print('|', n, 'X', i, '=', multipli)
    i += 1
print('-'*20)
