# Crie um programa que leia VÁRIOS NÚMEROS inteiros pelo teclado. 
# O programa só vai parar quando o usuário digitar o valor 999, que é a CONDIÇÃO DE PARADA. 
# No final, mostre QUANTOS NÚMEROS foram digitados e qual foi a SOMA entre eles (desconsiderando o flag)


num = soma = cont = 0
while True:
    num = int (input ('Digite um número [999 para parar]: '))
    if num == 999:
        break
    soma = (soma + num)
    cont = (cont + 1)
print (f'Foram digitados {cont} números e a soma foi {soma}')

