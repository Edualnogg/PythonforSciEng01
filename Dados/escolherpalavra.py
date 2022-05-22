
datas = []
for i in range(1):
    data = input('Seu email: ')
    if data.count('@') <1 or data.count('@') > 1:
        raise 'IncorrectEmail'
    elif data.count('.com') <1 or data.count('.com') > 1:
        raise 'IncorrectEmail'
    data1 = input('Sua senha: ')
    if len(data1) < 7:
        raise 'A senha tem que ter mais de 7 caracteres'
    datas.append(data)
    datas.append(data1)
    
data_user = {'senha': datas[0] , 'email': datas[1] }  



print(list(data_user.items()))