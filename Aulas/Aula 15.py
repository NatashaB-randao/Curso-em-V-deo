'''cont = 1
while True:                 # executar o que estiver dentro do While para sempre
    print (cont, '→', end=' ')
    cont = (cont + 1)
print ('Acabou')'''


'''n = cont = 0
while cont < 3:
    n = int (input ('Digite um número: '))
    cont = (cont + 1)'''

'''n = s = 0
while n != 999:
    n = int (input ('Digite um número: '))
    s = (s + n)
print ('A soma vale {}'.format (s))'''


'''n = s = 0
while True:
    n = int (input ('Digite um número: '))
    if n == 999:
        break
    s = (s + n)
# print ('A soma vale {}'.format (s))       # PYTHON 3
print (f'A soma vale {s}')'''               # f-string

nome = 'José'
idade = 38
salário = 938.3
print (f'O {nome} tem {idade} anos e ganha R${salário:.2f}')                # PYTHON 3.6 +
   