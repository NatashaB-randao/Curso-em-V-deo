# A confederação nacional de natação precisa de um programa que leia:
# O ANO DE NASCIMENTO de um atleta e mostre sua CATEGORIA, de acordo com a IDADE:
# ATÉ 9 anos: MIRIM
# ATÉ 14 anos: INFANTIL
# ATÉ 19 anos: JÚNIOR
# ATÉ 20 anos: SÊNIOR
#ACIMA: MASTER

from datetime import date
ano_atual = date.today ().year
ano_nascimento = int (input ('Ano de nascimento do atleta: '))
idade = ano_atual - ano_nascimento
print ('Quem nasceu em {} tem {} anos em {}'.format (ano_nascimento, idade, ano_atual))
if idade <=9:
    print('A categoria do atleta é MIRIM')
elif idade >9 and idade <=14:
    print ('A categoria do atleta é INFANTIL')
elif idade >14 and idade <=19:
    print ('A categoria do atleta é JÚNIOR')
elif idade == 20:
    print ('A categoria do atleta é SÊNIOR')
else:
    print ('A categoria do atleta é MASTER')
