# Faça um programa que leia de 0 a 9999 emostre na tela cada um dos dígitos separados
# Ex.: Digite um número: 1834
'''unidade: 4
   dezena: 3
   centena: 8
   milhar: 1 '''
   
'''numero = int (input ('Digite um número de 0 à 9999 '))
num = str (numero)
print ('Analisando o número {}'.format (numero))
print ('Unidade {}'.format (num [3]))
print ('Dezena {}'.format (num [2]))
print ('Centena'.format (num [1]))
print ('Milhares {}'.format (num [0]))'''

numero = int (input ('Digite um número de 0 à 9999 '))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhares = numero // 1000 % 10
print ('Analisando o número {}'.format (numero))
print ('Unidade {}'.format (unidade))
print ('Dezena {}'.format (dezena))
print ('Centena {}'.format (centena))
print ('Milhares {}'.format (milhares))

