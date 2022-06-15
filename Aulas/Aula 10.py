'''nome = str (input('Qual é o seu nome? '))
if nome == 'Gustavo':
    print ('Que nome lindo você tem!')
else:
    print ('Seu nome é tão normal!')
print ('Bom dia, {}'.format(nome))'''

nota1 = float (input('Digite a primeira nota: '))
nota2 = float (input('Digite a segunda nota: '))
média = (nota1 + nota2) / 2
print ('A sua média foi {:.1f}'.format(média))
if média >= 6.0:
    print ('Sua média foi boa! PARABÉNS!')
else:
    print ('Sua média foi ruim')
