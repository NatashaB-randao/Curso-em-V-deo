'''num = [2,5,9,1]
print(num)'''

'''num = [2,5,9,1]
num[2] = 3
print(num)'''

'''num = [2,5,9,1]
num[2] = 3
num.append(7)
print(num)'''

'''num = [2,5,9,1]
num[2] = 3
num.append(7)
num.sort()
print(num)'''

'''num = [2,5,9,1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
print(num)'''

'''num = [2,5,9,1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
print(num)
print(f'Essa lista tem {len(num)} elementos')'''

'''num = [2,5,9,1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2,0)         # na posição 2 inserir o valor 0
print(num)
print(f'Essa lista tem {len(num)} elementos')'''

'''num = [2,5,9,1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2,0) 
num.pop()        
print(num)
print(f'Essa lista tem {len(num)} elementos')'''

'''num = [2,5,9,1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2,0) 
num.pop(2)        
print(num)
print(f'Essa lista tem {len(num)} elementos')'''

'''num = [2,5,9,1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2,2)      
num.remove(2)   
print(num)
print(f'Essa lista tem {len(num)} elementos')'''

'''num = [2,5,9,1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2,2)      
num.remove(4)   
print(num)
print(f'Essa lista tem {len(num)} elementos')'''

'''num = [2,5,9,1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2,2)      
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')  
print(num)
print(f'Essa lista tem {len(num)} elementos')'''

'''valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):         # C = índice/chaves
    print(f'Na posição {c} encontrei o valor {v}...')
print('Cheguei ao final da lista')'''

'''valores = []
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):         # C = índice/chaves
    print(f'Na posição {c} encontrei o valor {v}...')
print('Cheguei ao final da lista')'''

'''a = [2, 3, 4, 7]
b = a               # está fazenda uma ligação entre as duas listas
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')'''

a = [2, 3, 4, 7]
b = a [:]             # está fazenda uma cópia da lista (b está recebendo todos os itens de A)
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
