# Faça um programa que leia o PESO de CINCO PESSOAS. 
# No final, mostre qual foi o MAIOR e o MENOR peso lidos

maior = 0
menor = 0
for p in range (1,6):
    peso = float (input ('Digite o peso da {}ª pessoa: '.format (p)))
    if p == 1:          #peso da primeira pessoa (se for a primeira pessoa, ela é a mais pesada e a mais leve)
        maior = peso
        menor = peso
    else:               #se não for a primeira pessoa
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print ('O maior peso lido foi de {}Kg'.format (maior))
print ('O menor peso lido foi de {}Kg'.format (menor))
