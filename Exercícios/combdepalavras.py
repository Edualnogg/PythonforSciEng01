# DESAFIO DE COMBINAÇÕES

lista_de_letras = ['A', 'R', 'A', 'R', 'A']
lista_de_palavras = []
iteracoes = 0

for i5 in range(len(lista_de_letras)):
    L5 = lista_de_letras[i5]
    lista_L5 = lista_de_letras.copy()
    lista_L4 = lista_L5.copy()
    lista_L4.pop(i5)

    for i4 in range(len(lista_L4)):
        L4 = lista_L4[i4]
        lista_L3 = lista_L4.copy()
        lista_L3.pop(i4)

        for i3 in range(len(lista_L3)):
            L3 = lista_L3[i3]
            lista_L2 = lista_L3.copy()
            lista_L2.pop(i3)

            for i2 in range(len(lista_L2)):
                L2 = lista_L2[i2]
                lista_L1 = lista_L2.copy()
                lista_L1.pop(i2)

                for i in range(len(lista_L1)):
                    L1 = lista_L1[i]
                    palavra = L5 + L4 + L3 + L2 + L1

                    # mostra o número total de combinações, considerando as repetidas
                    iteracoes += 1

                    # CONDIÇÃO PARA NÃO REPETIR A PALAVRA
                    if palavra not in lista_de_palavras:
                        lista_de_palavras.append(palavra)
print(lista_de_palavras)
print('O número de combinações é {}'.format(len(lista_de_palavras)))
print('\033[1;30;41m A quantidade total de combinações, considerando as repetidas é de {} \033[m'.format(iteracoes))


'''
ESSA CONDIÇÃO ACIMA FAZ O SEGUINTE COMANDO --->

O L5 PEGA A PRIMEIRA LETRA DA LISTA
A LISTA DE LETRAS É COPIADA PARA A LISTA_L5
A LISTA_L5 É COPIADA PARA A LISTA_L4
A LISTA_L4 RETIRA O PRIMEIRO ELEMENTO DA LISTA, DEVIDO O FOR
'''
