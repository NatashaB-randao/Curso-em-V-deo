# Crie um programa que leia o ANO DE NASCIMENTO de SETE PESSOAS
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores


from datetime import date
ano_atual = date.today().year
total_maior = 0
total_menor = 0
for pessoa in range (1, 8):
    ano_nascimento = int (input ('Em que ano a {}ª pessoa nasceu? '.format (pessoa)))
    idade = ano_atual - ano_nascimento
    if idade >= 18:
        total_maior = total_maior + 1
    else:
        total_menor = total_menor + 1
print ('Ao todo, tivemos {} pessoas maiores de idade'.format (total_maior))
print ('E, também, tivemos {} pessoas menores de idade'.format (total_menor))
