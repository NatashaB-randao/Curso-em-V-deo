# === Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento ===
salário = float (input ('Digite o salário atual do funcionário: R$ '))
reajuste = salário + (salário * 15 / 100)
print ('O funcionário que ganhava o salário de R${:.2f}, após o aumento de 15% receberá R${:.2f}'.format(salário, reajuste))

