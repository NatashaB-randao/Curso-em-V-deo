# Crie um programa onde o usuário possa digitar 5 VALORES NUMÉRICOS e CADASTRE-OS em uma LISTA, JÁ NA POSIÇÃO CORRETA de inserção (sem usar o sort())
# No final, mostre a lista ORDENADA na tela.

lista = list()
for c in range(0,5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[len(lista)-1] :      # Se for o primeiro valor ou se o número for maior do que o número que está no último elemento
        lista.append(n)
        print('Adicionado no final da lista')
    else:
        posição = 0
        while posição < len(lista):     #vai da posição 0 até a última posição
            if n <= lista[posição]:
                lista.insert(posição, n)
                print(f'Adicionado na posição {posição} da lista')
                break
            posição += 1
print('-='*30)
print(f'Os valores digitados em ordem foram: {lista}')

      
           