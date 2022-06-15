# Crie um programa que vai ler VÁRIOS NÚMEROS e colocar em uma lista.
# Depois disto crie DUAS LISTAS EXTRAS que vão contar apenas os valores PARES e ÍMPARES digitados, respectivamente.
# Ao final, mostre o conteúdo das TRÊS LISTAS geradas.

num = list()        #vetor
pares = list()      #vetor
ímpares = list ()   #vetor
while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
for i, v in enumerate(num):      #índece e valor
    if v % 2 == 0:
        num.sort()
        pares.append(v)
    else:
        num.sort()
        ímpares.append(v)
num.sort()
print('-='*30)
print(f'A lista completa é {num} ')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {ímpares}')


