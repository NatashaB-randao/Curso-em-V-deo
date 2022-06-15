# === Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado ===
# === Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado ===
km_percorridos = float (input ('Digite a quantidade de km percorridos pelo carro: '))
dias = int (input ('Digite a quantidade de dias que o carro foi alugado: '))
preço_a_pagar = (60 * dias) + (0.15 * km_percorridos)
print ('O preço a pagar pelo aluguel será R$ {:.2f}'.format(preço_a_pagar))

