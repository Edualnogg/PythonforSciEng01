print('-'*23)
print('| ANALISADOR DE DADOS |')
print('-'*23)

print('Esse progragama analisa a quantidade de\num valor que você deseja, basta adicionar onde pede.\n\n')


# entrada de dados
dados = input('Cole o arquivo que deseja analisar: ')
data = input('Digite exatamente o que deseja encontrar: ')

# função  que conta a variável desejada


def contagem_valores(lista, variavel):
    for i in lista:
        qnt = lista.count(str(variavel))
    print(f'Os dados contém {qnt} valores correspondentes')


# saída de dados
teste = contagem_valores(dados, data)
print(teste)
