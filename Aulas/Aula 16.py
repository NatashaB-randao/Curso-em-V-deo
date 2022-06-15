'''lanche = ('hanburguer', 'suco', 'pizza', 'pudim')       #variável composta (tupla)
print(lanche)'''

'''lanche = ('Hanburguer', 'Suco', 'Pizza', 'Pudim')       
print(lanche[1])'''


'''lanche = ('Hanburguer', 'Suco', 'Pizza', 'Pudim')       
print(lanche[-2])'''

'''lanche = ('Hanburguer', 'Suco', 'Pizza', 'Pudim')       
print(lanche[1:3])'''

'''lanche = ('Hanburguer', 'Suco', 'Pizza', 'Pudim')       
print(lanche[2:])'''

'''lanche = ('Hanburguer', 'Suco', 'Pizza', 'Pudim')       
print(lanche[:2])'''

'''lanche = ('Hanburguer', 'Suco', 'Pizza', 'Pudim')       
print(lanche[-2:])'''

'''lanche = ('Hanburguer', 'Suco', 'Pizza', 'Pudim')       
print(lanche[-3:])'''

'''lanche = ('Hanburguer', 'Suco', 'Pizza', 'Pudim')      
#Tuplas são IMUTÁVEIS 
lanche[1] = 'refrigerante'          #comando errado (não pode ser executado)
print(lanche[1])'''

'''lanche = ('Hanburguer', 'Suco', 'Pizza', 'Pudim')       
for comida in lanche:
    print(f'Eu vou comer {comida}')'''

'''lanche = ('Hanburguer', 'Suco', 'Pizza', 'Pudim')
print (len(lanche))'''

'''lanche = ('Hanburguer', 'Suco', 'Pizza', 'Pudim')
for cont in range (0, len(lanche)):
    print(lanche[cont])'''

'''lanche = ('Hanburguer', 'Suco', 'Pizza', 'Pudim')
for cont in range (0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')'''

'''lanche = ('Hanburguer', 'Suco', 'Pizza', 'Pudim')
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')'''

'''lanche = ('Hanburguer', 'Suco', 'Pizza', 'Pudim')
for cont in range (0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')'''

'''lanche = ('Hanburguer', 'Suco', 'Pizza', 'Pudim')
print (sorted(lanche))'''          #sorted = organizado, em ordem (não altera a tupla, apenas coloca em ordem)

'''a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print (c)'''

'''a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print (len(c))'''

'''a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print (c.count(5))'''

'''a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print (c.index(8))'''             #index = mostra a posição

pessoa = ('Natasha', 22, 'F', 56)
del(pessoa)                         #del = apagar uma variável
print (pessoa)