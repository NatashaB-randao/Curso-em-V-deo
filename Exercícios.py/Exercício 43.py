# Desenvolva uma lógica que leia o PESO e a ALTURA de uma pessoa
# Calcule o seu IMC e mostre seu status de acordo com a tabela abaixo:
# ABAIXO de 18.5: ABAIXO DO PESO
# ENTRE 18.5 e 25: PESO IDEAL
# 25 ATÉ 30: SOBREPESO
# 30 ATÉ 40: OBESIDADE 
# ACIMA de 40: OBESIDADE MÓRBIDA

peso = float (input ('Qual é o seu peso? (kg) '))
altura = float (input ('Qual é a sua altura? (m) '))
imc = peso / (altura**2)
print ('O IMC dessa pessoa é de {:.1f}'.format (imc))
if imc < 18.5:
    print ('Você está abaixo do peso normal!')
elif imc >= 18.5 and imc <=25:
    print ('Você está no peso ideal!')
elif imc >25 and imc <=30:
    print ('Você está no sobrepeso!')
elif imc >30 and  imc <=40:
    print ('Você está na faixa de obesidade!')
else:
    print ('Você está na faixa de obesidade mórbida!')
