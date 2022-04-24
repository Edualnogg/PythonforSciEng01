'''
(tuple)	tupla: uma sequência de dados que é imutável --->  vogais = ('a','e','i','o','u')
(set)	conjunto: elementos não possuem ordem e não se repetem	alg_decimais = {0,1,2,3,4,5,6,7,8,9}
(dict)	dicionário: são indexaxos por uma chave keys	alg_romanos = {'I':1,"II":2,'III':3,'IV':4,'V':5,'X':10}

'''
# tem que ser entre parenteses e é imutável, não posso substituir nada 
vogais = ('a','e','i','o','u')

print(len(vogais))
print('-'*10)


#-------------------------------------#

vogais_list = ['a','e','i','o','u']

for i in enumerate(vogais_list):
    print(i[1])
    
    
#-------------------------------------#

# tb é imutável e indexável, a ordem tb não importa
set_variaveis = {'e','i','o','a'}
print(set_variaveis)

#-------------------------------------#

dict_1 = {'dia':10,'mes':5}
print(dict_1['mes'])
