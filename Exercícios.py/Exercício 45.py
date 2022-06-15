# Crie um programa que faça o computador jogar JOKEMPÔ com você
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint (0, 2)
print ('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int (input ('Qual é a sua jogada? '))
print ('JO')
sleep (1)
print ('KEM')
sleep (1)
print ('PÔ!!!')
sleep (1)

print ('-=' * 15)
print ('O computador escolheu {}'.format (itens [computador]))
print ('O jogador escolheu {}'.format (itens [jogador]))
print ('-=' * 15)

if computador == 0:     # computador jogou Pedra
    if jogador == 0:
        print ('EMPATE!')
    elif jogador == 1:
        print ('O Você GANHOU!')
    elif jogador == 2:
        print ('O Computador GANHOU!')
    else:
        print ('Jogada inválida!')

elif computador == 1:   # computador jogou Papel
    if jogador == 0:
        print ('O Computador GANHOU')
    elif jogador == 1:
        print ('EMPATE!')
    elif jogador == 2:
        print ('Você GANHOU!')
    else:
        print ('Jogada inválida!')

elif computador == 2:   # computador jogou Tesoura
    if jogador == 0:
        print ('Você GANHOU!')
    elif jogador == 1:
        print ('O Computador GANHOU!')
    elif jogador == 2:
        print ('EMPATE!')
    else:
        print ('Jogada inválida!')
