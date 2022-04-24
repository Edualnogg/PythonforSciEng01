# Formas de trabalhar com listas

'''
range(inteiro)	retorna um iterável do tipo range
lambda x: função_x	Retorna uma função
map(função,lista)	Retorna um iterável do tipo map
list(iterável)	Cria uma lista a partir de um iterável

'''

lista_quadrados = []

for i in range(5):
    lista_quadrados.append(i**2)
print(lista_quadrados)

#-----------------------------------------#

numeros = [1,2,3,4,5]

# y em função de x
f = lambda x:x**2
lista_5 = list(map(f,numeros))
print(lista_5)

#obs: o map irá fazer um iterável com os números da lista de acordo com a função 'f'

#-----------------------------------------#

# mais simplificado
quadrados = [x**2 for x in range(5)]
print(quadrados)
