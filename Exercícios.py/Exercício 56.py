# Faça um programa que leia NOME, IDADE e SEXO de 4 PESSOAS. 
# No final do programa, mostre:
# A MÉDIA DE IDADE do grupo;
# Qual é o nome do homem MAIS VELHO;
# Quantas mulheres têm MENOS de 20 anos

soma_idade = 0
média_idade = 0
maior_idade_homem = 0
nome_mais_velho = ''
total_mulher_20 = 0
for p in range (1, 5):
    print ('----- {}ª PESSOA -----'.format (p))
    nome = str (input ('NOME: ')).strip()
    idade = int (input ('IDADE: '))
    sexo = str (input ('SEXO: [F/M] ')).strip()
    soma_idade = soma_idade + idade

    if p == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_mais_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_mais_velho = nome
    if sexo in 'Ff' and idade < 20:
        total_mulher_20 = total_mulher_20 + 1

média_idade = (soma_idade / 4)

print ('A média de idade do grupo é de {} anos'.format (média_idade))
print ('O homem mais velho tem {} anos e se chama {}'.format (maior_idade_homem, nome_mais_velho))
print ('Ao todo são {} mulheres com menor de 20 anos'.format (total_mulher_20))