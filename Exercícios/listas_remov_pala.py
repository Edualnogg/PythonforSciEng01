# ESSE CÓDIGO REMOVE AS LETRAS EXTRAS E ESPAÇOS DA LISTA

lista = ['P', 'A', 'Y', 'A', 'T', 'A', 'H', 'O', 'N']
palavra = ''
for i in lista:
    if i == 'A':
        lista.remove('A')
for j in lista:
    x = j
    palavra += x
print(palavra)
