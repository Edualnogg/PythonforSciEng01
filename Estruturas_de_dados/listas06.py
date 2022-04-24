'''
.items()	Retorna os itens do dicionário
.keys()	Retorna as chaves do dicionário
.values()	Retorna as chaves do dicionário
.pop(key)	Remove a chave especificada e retorna o valor do item
.copy()	Retorna uma cópia
.clear()	Remove os itens
.get(key)	Retornas a váriável em key

'''
#---------------------------------------------------#

alg_romanos = {'I': 1, 'II': 2, 'III': 3, 'IV': 4}

a = alg_romanos.pop('IV')
print(alg_romanos)

print(list(alg_romanos.items()))
print(list(alg_romanos.keys()))
print(list(alg_romanos.values()))
a = alg_romanos.get('I')
print(a)
