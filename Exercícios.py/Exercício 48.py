#Faça um programa que calcule a SOMA entre todos os NÚMEROS ÍMPARES que são MÚLTIPLOS de 3
# E que se encontram no intervalo de 1 até 500

soma = 0            #acumulador
cont = 0             #contador
for c in range (1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print (' A soma de todos os {} valores solicitados é {}'.format (cont, soma))
