
# Crie um programa que vai gerar CINCO NÚMEROS ALEATÓRIOS e colocar em uma TUPLA
# Depois disso, mostre a LISTAGEM DE NÚMEROS gerados e também indique o MENOR e o MAIOR valor que estão na tupla 


from random import randint
números = (randint(1,10), randint(1,10),  randint(1,10), randint(1,10), randint(1,10))
#print (f'Eu sortei os valores {números}')
print (' Os valores sorteados foram: ', end= ' ')
for n in números:
    print (f'{n} ', end= ' ')
print (f'\n O maior valor sorteado foi {max(números)}')
print (f' O menor valor sorteado foi {min(números)}')