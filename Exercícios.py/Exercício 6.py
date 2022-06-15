# ==== Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada ====
num = int (input ('Digite um número: '))
dobro = num * 2
triplo = num * 3
raiz = num**(1/2)
print ('O dobro do número {} é {}, o triplo é {} e a raiz quadrada é {:.2f}'.format(num, dobro, triplo, raiz))
