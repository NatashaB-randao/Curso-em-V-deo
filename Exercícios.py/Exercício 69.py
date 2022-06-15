# Crie um programa que leia a IDADE e o SEXO de VÁRIAS PESSOAS. 
# A cada pessoa cadastrada, o programa deverá perguntar se o USUÁRIO quer ou não continuar. No final mostre:
# A) Quantas pessoas têm mais de 18 anos
# B) Quantos HOMENS foram cadastrados
# C) Quantas MULHERES têm menos de 20 anos


total_18 = total_homens = total_mulheres20  = 0
while True:                         #LER OS DADOS (até linha 13)
    idade = int (input ('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str (input ('Sexo: [M/F] ')).strip().upper() [0]
    if idade >= 18:
        total_18 = (total_18 + 1)
    if sexo == 'M':
        total_homens = (total_homens + 1)
    if sexo == 'F' and idade < 20:
        total_mulheres20 = (total_mulheres20 + 1)
    resposta = ' '                  #PERGUNTAR SE VAI CONTINUAR OU NÃO
    while resposta not in 'SN':
        resposta = str (input ('Deseja continuar? [S/N] ')).strip().upper() [0]
    if resposta == 'N':
        break
print (f'Total de pessoas com mais de 18 anos: {total_18}')
print (f'Ao todo {total_homens} homens cadastrados')
print (f'E temos {total_mulheres20} mulheres com menos de 20 anos')
