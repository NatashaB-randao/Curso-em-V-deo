# Crie um programa que simule o funcionamento de um CAIXA ELETRÔNICO. 
# No início, pergunte ao usuário qual será o VALOR A SER SACADO (número inteiro) 
# E o programa vai informar quantas CÉDULAS de cada valor serão entregues. 
# OBS.: considere que o caixa possui dédulas de R$50.00, R$20.00, R$10.00 e R$1.00

print ('='*30)
print ('{:^30}'.format ('BANCO NB'))
print ('='*30)
valor = int(input('Qual valor deseja sacar? R$ '))
total = valor
cédula = 50
total_cédula = 0
while True:
    if total >= cédula:                             #quantas vezes eu consigo tirar 50 do total
        total = (total - cédula)
        total_cédula = (total_cédula + 1)
    else:                                           #se não der para tirar 50, verificar o valor da cédula atual
        if total_cédula > 0:
            print (f'Total de {total_cédula} cédula(s) de R${cédula}')
        if cédula == 50:
            cédula = 20
        elif cédula == 20:
            cédula = 10
        elif cédula == 10:
            cédula = 1
        total_cédula = 0
        if total == 0:
            break
print ('='*30)
print ('Volte sempre ao BANCO NB!')

