# === Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar. ===
# === Considere US$1,00 = R$3,27
real = float (input ('Digite o valor em Reais R$: '))
dólar = real / 5.65
euro = real / 6.77
print ('Com R$ {:.2f} você pode comprar US$ {:.2f} e EUR {:.2f}'.format(real, dólar, euro))

