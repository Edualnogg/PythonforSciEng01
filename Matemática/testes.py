def media(lista):
    soma = sum(lista)
    n_de_valores = 0
    for i in lista:
        n_de_valores += 1
    media = (soma/n_de_valores)
    return f'{media}'


def variancia(lista):
        media1 = float(media(lista))
        v = []
        j = 0
        for i in lista:
              vr = float((i - media1)**2)
              v.append(vr)
              j+=1
        tot_list = sum(v)
        vari = float(tot_list/j)
        return f'{vari:.2}'


def dp(lista):
        dp1 = float(variancia(lista))
        dp = ((dp1)**(1/2))
        return f'{dp:.2}'


amostras = [21,15]
#print(variancia(amostras))
print(media(amostras))
#print(dp(amostras))