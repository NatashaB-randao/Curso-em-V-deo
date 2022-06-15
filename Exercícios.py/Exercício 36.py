# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa
# O programa vai perguntar o VALOR DA CASA, o SALÁRIO do comprador e em QUANTOS ANOS ele vai pagar
# Calcule o valor da prestação mensal, sabendo que não pode exceder 30% do salário ou então o empréstimo será negado. 

valor_casa = float (input ('Qual o valor da casa? R$'))
salário = float (input ('Qual é o seu salário? R$'))
anos = float (input ('Em quantos anos será realizado o pagamento? '))
prestação_mensal = (valor_casa) / (anos*12)
mínimo = salário * 30 / 100
print ('Para pagar a casa com valor de R${:.2f} em {:.0f} anos, a prestação mensal será de R${:.2f}'.format (valor_casa, anos, prestação_mensal))
if prestação_mensal <= mínimo:
    print ('O empréstimo pode ser concedido!')
else:
    print ('Empréstimo negado!')
