# Desenvolva um programa que leia 4 valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# a) quantas vezes apareceu o número 9;
# b) em que posição foi digitado o primeiro valor 3;
# c) quais foram os números pares

núm = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')), 
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
print(f'Você digitou os valores {núm}')
print(f'O valor 9 apareceu {núm.count(9)} vez(es)')
if 3 in núm:
    print(f'O valor 3 apareceu na {núm.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram ', end= '')
for n in núm:
    if n % 2 == 0:
        print(n, end=' ')