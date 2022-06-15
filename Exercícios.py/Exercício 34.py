# Escreva um programa que pergunte o salário do funcionário e calcule o valor do seu aumento. 
# Para salários superiores a R$ 1250,00, calcule um aumento de 10%
# Para salários inferiores ou iguais o aumento é de 15%

salário = float (input ('Digite o salário do funcionário: R$'))
if salário > 1250:
    reajuste = salário + (salário * 10) / 100
    print ('Quem ganhava {:.2f} passará a ganhar {:.2f}'.format (salário, reajuste))
else:
    reajuste = salário + (salário * 15) /100
    print (' Quem ganhava R${:.2f} passará a ganhar R${:.2f}'.format (salário, reajuste))
