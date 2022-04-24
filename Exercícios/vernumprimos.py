# verificando números primos

lista_numeros_primos = [2]
proximo_elemento = 2

while len(lista_numeros_primos) < 50:
    # adiciona 1 elemento a mais em cada rodada
    proximo_elemento += 1
    proximo_elemento_status = ''

    for elemento in lista_numeros_primos:
        # pega um elemento e divide por ele mesmo
        quociente = proximo_elemento / elemento
        # divide o elemento pelo o  sucessor
        quociente_inteiro = proximo_elemento // elemento

        # se a divisão entre quoc. int e quoc forem iguais(4/2=2 ; 4//2=2), não é n° primo --->
        # sempre dividindo pela lista [2]
        # (3/2=1,5 ; 3//2=1) se for diferente é um número primo 
        if quociente_inteiro == quociente:
            proximo_elemento_status = 'Pula'
            break

    if proximo_elemento_status == 'Pula':
        continue
    else:
        lista_numeros_primos.append(proximo_elemento)
        
print(lista_numeros_primos)


