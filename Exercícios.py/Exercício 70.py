# Crie um programa que leia o NOME e o PREÇO de VÁRIOS PRODUTOS. 
# O programa deverá perguntar se o USUÁRIO vai continuar. No final, mostre:
# A) Qual é o TOTAL GASTO na compra
# B) Quantos produtos custam MAIS de R$ 1000,00
# C) Qual é o NOME do produto mais BARATO 


total = tot1000 = cont = menor = 0
barato = ' '
while True:
    produto = str (input ('Digite o nome do produto: '))
    preço = float (input ('Digite o preço do produto: '))
    cont = (cont + 1)
    total = (total + preço)
    if preço > 1000:
        tot1000 = (tot1000 + 1)
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resposta = ' '                  #PERGUNTAR SE VAI CONTINUAR OU NÃO
    while resposta not in 'SN':
        resposta = str (input ('Deseja continuar? [S/N] ')).strip().upper() [0]
    if resposta == 'N':
        break
print ('{:-^40}'.format (' FIM DO PROGRAMA '))
print (f'O total gasto foi de R$ {total:.2f}')
print (f'Temos {tot1000} produto(s) custando mais de R$1000.00')
print (f'O produto mais barato foi {barato} que custa R$ {menor:.2f}')
