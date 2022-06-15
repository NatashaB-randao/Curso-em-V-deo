# Faça um programa que leia um NÚMERO INTEIRO e diga se ele é ou não um NÚMERO PRIMO


num = int (input ('Digite um número inteiro: '))
total = 0
for c in range (1, num + 1):
    if num % c == 0:
        total = total + 1
    print ('{}'.format (c), end=' ')
print ('\nO número {} foi divisível {} vezes'.format (num, total))
if total == 2:
    print ('E por isso ele É PRIMO')
else:
    print ('E por isso ele NÃO É PRIMO')