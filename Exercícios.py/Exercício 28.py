# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual o número escolhido pelo computador
# O programa deverá escolher na tela se o usuário venceu ou perdeu

from random import randint
from time import sleep
computador = randint (0, 5)  #Faz o computador "pensar"
print ('-=-' * 20 )
print ('Vou pensar em um número entre 0 e 5, tente adivinhar...')
print ('-=-' * 20 )
jogador = int (input (' Em que número eu pensei? ')) #jogador tenta adivinhar
print ('Processando...')
sleep (2)
if jogador == computador:
    print ('Você conseguiu me vencer! PARABÉNS!')
else:
    print ('Ganhei! Eu pensei no número {} e não no {}!'.format (computador, jogador))
