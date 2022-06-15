# Crie um programa que pergunte a distância da viagem em km. 
# Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200 km
# e R$ 0,45 para viagens mais longas

distância_km = float (input ('Digite a distância da viagem em km: '))
print ('Você irá realizar uma viagem de {} km'.format (distância_km))
if distância_km > 200:
    print ('A distância a ser percorrida será maior que 200 km')
    passagem = distância_km * 0.45
    print ('O valor da passagem será de R$ {:.2f}'.format (passagem))
else:
    passagem = distância_km * 0.50
    print ('O valor da passagem será de R$ {:.2f}'.format (passagem))
