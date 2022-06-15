# Crie um programa que leia VÁRIOS NÚMEROS inteiros pelo teclado. 
# O programa só vai parar quando o usuário digitar o valor 999, que é a CONDIÇÃO DE PARADA. 
# No final, mostre QUANTOS NÚMEROS foram digitados e qual foi a SOMA entre eles (desconsiderando o flag)


num = 0
cont = 0
soma = 0
num = int (input ('Digite um número [999 para parar]: '))
while num != 999:
    soma = (soma + num)
    cont = (cont + 1)
    num = int (input ('Digite um número [999 para parar]: '))
print ('Você digitou {} números e a soma entre eles foi {}'.format (cont,soma))