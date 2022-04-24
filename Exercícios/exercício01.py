# REMOVER OS 'A' EXCEDENTES

lista = ['P', 'A', 'Y', 'A', 'T', 'A', 'H', 'O', 'N']
c = lista.count('A')
print(c)

for i in range(c):
    lista.remove('A')
print(lista)
