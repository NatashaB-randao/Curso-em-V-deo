# Crie um programa que leia VÁRIOS NÚMEROS inteiros pelo teclado. 
# No final da execução, mostre a MÉDIA ENTRE TODOS os valores e qual foi o MAIOR e MENOR valores lidos. 
# O programa deve perguntar ao usuário se ele quer ou não CONTINUAR a digitar valores. 

resposta = 'S'
soma = 0
quantidade = 0
média = 0
maior = 0
menor = 0


while resposta in 'Ss':
    núm = int (input ('Digite um número: '))
    soma = (soma + núm)
    quantidade = (quantidade + 1)
    if quantidade == 1:
        maior = menor = núm
    else:
        if núm > maior:
            maior = núm
        if núm < menor:
            menor = núm
    resposta = str (input ('Quer continuar? [S/N] ')).upper().strip() [0]

média = (soma/quantidade)
print ('Você digitou {} números e a média foi {}'.format (quantidade, média))
print ('O maior valor foi {} e o menor valor foi {}'.format (maior, menor))
