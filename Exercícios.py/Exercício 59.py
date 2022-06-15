# Crie um programa que leia DOIS VALORES e mostre um MENU na tela:
# 1 [SOMAR]
# 2 [MULTIPLICAR]
# 3 [MAIOR]
# 4 [NOVOS NÚMEROS]
# 5 [SAIR DO PROGRAMA]

#Seu programa deverá realizar a operação solicitada em cada caso

from time import sleep
itens = ('Somar', 'Multiplicar', 'Maior', 'Maior', 'Novos números', 'Sair do programa')
maior = ''

for n in range (1, 3):
    número = int (input ('Digite o {}º número: '.format (n)))
print ('''MENÚ:
[ 0 ] SOMAR
[ 1 ] MULTIPLICAR
[ 2 ] MAIOR
[ 3 ] NOVOS NÚMEROS
[ 4 ] SAIR DO PROGRAMA ''')

escolher = int (input ('Qual opção do menú você deseja? '))
sleep (0.5)
print ('-' * 40)
print ('Você escolheu a opção: {}'.format (itens [escolher]))

if escolher == 0:
    somar = (número + número)
    print (somar)
elif escolher == 1:
    multiplicar = (número + número)
    print (multiplicar)
elif escolher == 2:
    maior = número
    print (maior)
