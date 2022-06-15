# Escreva um programa que leia a velocidade de um carro. 
# Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que ele foi multado
# A multa vai custar R$ 7,00 por cada km acima do limite

print ('A velocidade máxima é de 80km/h')
print ('--' * 20)
velocidade_carro = float (input ('Digite a velocidade do carro: '))
if velocidade_carro > 80:
    print ('Você ultrapassou a velocidade máxima! Você deverá pagar multa')
    multa = (velocidade_carro - 80) * 7
    print (' A multa será de R${:.2f}'.format (multa))
    print ('--' * 20)
else:
    print ('Você não ultrapassou a velocidade máxima. Não precisará pagar multa!')
