'''
.append(variável)	Adiciona a variável no final
.extend(outra_lista)	Adiciona os elementos ao final
.remove(variável)	Remove o primeiro elemento com valor variável
.count(variável)	Conta o número de elementos com o valor variável
.sort()	Reordena elementos em ordem numérica ou alfabética
.reverse()	Inverte a ordem dos elementos
.copy()	Retorna uma cópia da lista
.index(variável)	Retorna o índice da primeira variável da lista

'''

lista_inteiros = [1, 2, 3, 4, 5]
lista_inteiros.append(6)
print(lista_inteiros)
print(len(lista_inteiros))

print('\033[1;30;41m *-* \033[m'*7)

#---------------------------------------------------#


lista_inteiros = [1, 2, 3, 4, 5]
lista_2 = [6, 7, 8]
lista_inteiros.extend(lista_2)
print(lista_inteiros)
print(len(lista_inteiros))

print('\033[1;30;41m *-* \033[m'*7)

#---------------------------------------------------#

lista_letras = ['a','b','c','a','a']
# mostra a quantidade de 'a'
n_vezes = lista_letras.count('a')
print(n_vezes)

print('\033[1;30;41m *-* \033[m'*7)

#---------------------------------------------------#

lista_3 = [1,10,5,3,8]
# reagrupa em ordem os itens
lista_3.sort()
print(lista_3)

print('\033[1;30;41m *-* \033[m'*7)

#---------------------------------------------------#

# números como str, o pc mostra primeiro os números
lista_4 = ['a','b','c','a','a','10','1','5']
lista_4.sort()
print(lista_4)

