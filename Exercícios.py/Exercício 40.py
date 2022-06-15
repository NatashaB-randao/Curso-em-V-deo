# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando  uma mensagem no final de acordo com a média atingida
# Média ABAIXO DE 5.0: REPROVADO
# Média ENTRE 5.0 E 6.9: RECUPERAÇÃO
# Média 7.0 ou SUPERIOR: APROVADO

nota_1 = float (input ('Digite a primeira nota: '))
nota_2 = float (input ('Digite a segunda nota: '))
média = (nota_1 + nota_2) / 2
if média >=5 and média <7:
    print ('A média do aluno foi {}. Aluno em RECUPERAÇÃO'.format (média))
elif média < 5:
    print ('A média do aluno foi {}. Aluno REPROVADO'.format (média))
else:
    print ('A média do aluno foi {}. Aluno APROVADO'.format (média))
