# Faça um programa que leia um 'número' qualquer e mostre o seu FATORIAL
# Ex.: 5! = 5x4x3x2x1 = 120


'''from math import factorial
num = int (input ('Digite um número para calcular o seu fatorial: '))
f = factorial (num)
print ('O fatorial de {} é {}'.format (num, f))'''


num = int (input ('Digite um número para calcular o seu fatorial: '))
c = num             #contador
f = 1
print ('Calculando {}! = '.format (num), end =' ')      
while c > 0:
    print ('{}'.format (c), end =' ')
    print (' x ' if c > 1 else ' = ', end =' ')
    f = (f * c)
    c = (c - 1)
print ('{}'.format (f))