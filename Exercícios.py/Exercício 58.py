# Melhore o jogo do desafio ''28'' onde o computador vai "pensar" em um ''número entre 0 e 10''
# Só que agora, o jogador vai tentar adivinhar até acertar,
# Mostrando no final quantos palpites foram necessários para acertar

# Minha resolução:
'''from random import randint
from time import sleep
computador = randint (0, 5)             #Faz o computador "pensar"
print ('-=-' * 20 )
print ('Vou pensar em um número entre 0 e 5, tente adivinhar...')
print ('-=-' * 20 )
jogador = int (input (' Em que número eu pensei? '))        #jogador tenta adivinhar
tentativas = 0
print ('Processando...')
sleep (1)

while jogador != computador:
    jogador = int (input ('Errou, tente novamente! '))
    tentativas = tentativas + 1

print ('Você conseguiu me vencer! PARABÉNS!')
print ('Você precisou de {} tentativas para me vencer. '.format (tentativas))''' 


# Resolução Guanabara:

from random import randint
from time import sleep
computador = randint (0, 10) 
print ('Sou seu computador... Acabei de pensar em um número entre 0 e 10')
sleep (1)
print ('Será que você consegue adivinhar qual foi?')
sleep (1)
acertou = False
palpites = 0

while not acertou:
    jogador = int (input ('Qual é o seu palpite? '))
    palpites = palpites + 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print ('Mais... Tente mais uma vez!')
        elif jogador > computador:
            print ('Menos... Tente mais uma vez!')
print ('Acertou com {} palpites!'.format (palpites))

