n = int(input('Digite um número: '))


def sequec(x):
    b = ' '
    for i in range(x + 1):
        print((str(i) + str(b)) * i)


c = sequec(n)
print(c)
