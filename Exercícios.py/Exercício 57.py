# Faça um programa que leia o SEXO de uma pessoa, mas só aceite os valores "M" ou "F"
# Caso esteja errado, peça a digitação novamente até ter um valor correto


sexo = str (input ('Digite qual o seu sexo [M/F] ')).upper().strip() [0]
while sexo not in 'MF':
     sexo = str (input ('Dados inválidos, por favor informe seu sexo: ')).upper().strip() [0]
print ('Sexo {} registrado com sucesso. '.format (sexo))
