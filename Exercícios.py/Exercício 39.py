# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele AINDA VAI SE ALISTAR ao serviço militar
# Se é a HORA DE SE ALISTAR;
# Se já PASSOU DO TEMPO de alistamento
# O programa também deve mostrar o tempo que falta ou que passou do prazo

from datetime import date
ano_atual = date.today().year 
ano_nascimento = int (input ('Digite o ano em que você nasceu: '))
idade = ano_atual - ano_nascimento
print ('Quem nasceu em {} tem {} anos em {}'.format ( ano_nascimento, idade, ano_atual))
if idade == 18:
    print ('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print ('Ainda faltam {} anos para o alistamento.'.format (saldo))
    ano = ano_atual + saldo
    print ('Seu alistamento será em {}')
else:
    saldo = idade - 18
    print ('Você já deveria ter se alistado há {} anos.'.format (saldo))
    ano = ano_atual - saldo
    print ('Seu alistamento foi em {}'.format ())
