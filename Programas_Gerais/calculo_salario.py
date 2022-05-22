print('-'*43)
print('| --------> CÁLCULO DE SALÁRIO <--------  |')
print('-'*43)


s_hora = float(input('Quanto você ganha por hora? R$'))
h_traba = int(input('Quantas horas por mês você trabalha? '))
print(' | '*18)


s_bruto = (s_hora * h_traba)
im_rend, des_inss, des_sind,  = (
    (11/100)*s_bruto), ((8/100)*s_bruto), ((5/100)*s_bruto)
descontos = ((11/100)*s_bruto) + ((8/100)*s_bruto) + ((5/100)*s_bruto)
s_liquido = (s_bruto - descontos)

print('Seu salário bruto é de R${}\nO valor pago no imposto de renda é de R${}\nO valor pago para o sindicato é de R${}\nO salário líquido é de R${}'.format(
    s_bruto, des_inss, des_sind, s_liquido))
