#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma LISTA.
# Caso o número já exista lá dentro, ele NÃO SERÁ ADICIONADO.
# No final, serão exibidos todos os VALORES ÚNICOS digitados, em ORDEM CRESCENTE.

números = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in números:
        números.append(n)
        print('Valor adicionado com sucesso.')
    else:
        print('Valor duplicado! Náo vou adicionar...')
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print('-='*30)
números.sort()
print(f'Você digitou os valores {números}')