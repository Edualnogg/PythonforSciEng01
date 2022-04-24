# FUNÇÃO POP E COPY

a = [1, 2, 3]
b = a.copy() # copia a lista sem alterá-la
print(b)

c = a.pop()

print(c) # o c chama o último elemento
print(a) # retira o último elemento

c = a.pop(0) # se eu chamar .pop(0) ele vai chamar o primeiro
print(c)
print(a) # retira o último elemento
