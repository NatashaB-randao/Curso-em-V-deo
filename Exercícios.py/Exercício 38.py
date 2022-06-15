# Escreva um programa que leia DOIS NÚMEROS INTEIROS e compare-os, mostrando na tela uma mensagem:
# O PRIMEIRO valor é MAIOR
# O SEGUNDO  valor é MAIOR
# NÃO EXISTE valor maior, os dois são IGUAIS

número_1 = int (input ('Digite um número inteiro: '))
número_2 = int (input ('Digite outro número inteiro: '))
if número_1 > número_2:
    print ('O PRIMEIRO valor é maior')
elif número_2 > número_1:
    print ('O SEGUNDO valor é maior')
else:
    print ('NÃO EXISTE valor maior, os dois são IGUAIS!')
