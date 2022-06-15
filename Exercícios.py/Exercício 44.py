# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu PREÇO NORMAL e CONDIÇÃO DE PAGAMENTO:
# À VISTA DINHEIRO/CHEQUE: 10% de desconto
# À VISTA no CARTÃO: 5% de desconto
# EM ATÉ 2X NO CARTÃO: PREÇO NORMAL
# 3X OU MAIS NO CARTÃO: 20% de JUROS

print ('{:=^40}'.format (' LOJAS GUANABARA '))
preço = float (input ('Preço das compras: R$'))
print ('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro ou cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int (input ('Qual é a opção? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
    print ('Sua compra de R${:.2f} vai custar R$ {:.2f} no final'.format (preço, total))
elif opção == 2:
    total = preço - (preço * 5 / 100)
    print ('Sua compra de R${:.2f} vai custar R$ {:.2f} no final'.format (preço, total))
elif opção == 3:
    total = preço
    parcela = total / 2
    print ('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format (parcela))
    print ('Sua compra de R${:.2f} vai custar R$ {:.2f} no final'.format (preço, total))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    total_parcelas = int (input ('Quantas parcelas? '))
    parcela = total / total_parcelas
    print ('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format (total_parcelas, parcela))
    print ('Sua compra de R${:.2f} vai custar R$ {:.2f} no final'.format (preço, total))
else:
    print ('Você deve escolher entre as opções 1,2,3 e 4')

