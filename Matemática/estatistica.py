

# função média
def media(lista):
    soma = sum(lista)
    n_de_valores = 0
    for i in lista:
        n_de_valores += 1
    media = float(soma/n_de_valores)
    return f'{media}'

# função mediana
def mediana(lista):
    lista.sort()
    n_de_valores = 0
    for i in lista:
        n_de_valores += 1
    if n_de_valores % 2 == 0:
        metade = int(n_de_valores/2)
        median = ((lista[metade-1]) + (lista[metade]))/2
        if n_de_valores == 2:
            mddd = media(lista)
            return mddd
        else:
            return f'{median}'
    else:    
        md = float(n_de_valores/2)
        md1 = int(md - (1/2))
        median2 = lista[md1]
        return f'{median2}'

#função variância
def variancia(lista):
        media1 = float(media(lista))
        v = []
        j = 0
        for i in lista:
              vr = float(((i+1) - media1)**2)
              v.append(vr)
              j+=1
        tot_list = sum(v)
        vari = float(tot_list/j)
        return f'{vari}'

#função dp
def dp(lista):
        dp1 = float(variancia(lista))
        dp = ((dp1)**(1/2))
        return f'{dp}'

amostras = []


print('-'*31)
print('| PROGRAMA ESTATÍSTICO BÁSICO |')
print('-'*31)
print('*-*'*15)

condicional = int(input('Quantos dados pretende adicionar? '))
for i in range(1, condicional+1):
    data = int(input('Adicione um dado: '))
    amostras.append(data)
    
print('*-*'*15)   




print(f'Média => {media(amostras):.7}\nMediana => {mediana(amostras):.7}\nVariância => {variancia(amostras):.7}\nDp => {dp(amostras):.7}')

