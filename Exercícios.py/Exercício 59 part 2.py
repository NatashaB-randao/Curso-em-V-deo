
from time import sleep
n1 = int (input ('Primeiro número: '))
n2 = int (input ('Segundo número: '))
opção = 0

sleep (1)
while opção != 5:
    print ('''MENÚ:
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA ''')

    sleep (1)

    opção = int (input ('Qual opção do menú você deseja? '))
    
    if opção == 1:
        somar = (n1 + n2)
        print ('A soma entre {} + {} é igual a: {}'.format (n1, n2, somar))
    elif opção == 2:
        produto = (n1 * n2)
        print ('O resultado de {} x {} é igual a: {}'.format (n1, n2, produto ))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print ('Entre {} e {} o maior valor é {}'.format (n1, n2, maior))
    elif opção == 4:
        print ('Informe os números novamente')
        n1 = int (input ('Primeiro número: '))
        n2 = int (input ('Segundo número: '))
    elif opção == 5:
        print ('Finalizando...')
    else:
        print ('Opção inválida! Tente novamente.') 
    print ('=-=' * 20)
    sleep (2)

print ('Fim do programa')
