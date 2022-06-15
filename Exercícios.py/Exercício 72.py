# Crie um programa que tenha uma TUPLA totalmente preenchida com uma contagem por extensão, de 0 até 20
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso


#tupla com contagem de zero a vinte
'''cont = ('zero', 'um', 'dois', 'três', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze', 'quatorze',
        'quinze', 'dezesseis', 'dezessete', 'dezoito',
        'dezenove', 'vinte')  
while True:                                                   #validação para ver se o número está dentro do limite
        num = int(input ('Digite um número entre 0 e 20: '))
        if 0 <= num <= 20:
                break
        print ('Tente novamente! ', end= '') 
print (f'Você digitou o número {cont[num]}')'''                 #escrever o número por extenso
                                                            #esse valor vai ser o elemento da tupla cont


n = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if num < 0 or num > 20:
        print('Invalido Tente novamente ', end='')
    else:
        print(f'Você digitou o número {n[num]}')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? S/N ')).upper().strip()[0]
    if resp == 'N':
        break
print('{:=^30}'.format(' PROGRAMA FINALIZADO '))
