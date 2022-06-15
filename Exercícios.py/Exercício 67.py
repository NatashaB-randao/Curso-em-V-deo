# Faça um programa que mostre a TABUADA de VÁRIOS NÚMEROS, um de cada vez para cada valor digitado. 
# O programa será interrompido quando o número solicitado for NEGATIVO. 


while True: 
    tabuada = int (input ('Qual tabuada você quer resolver? '))
    print ('-' * 30)
    if tabuada < 0:
        break
    for c in range (1, 11):
        print (f'{tabuada} x {c} = {tabuada*c}')
    print ('-' * 30)
print ('PROGRAMA TABUADA ENCERRADO')