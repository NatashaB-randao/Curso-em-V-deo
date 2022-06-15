# === Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa ===
'''co = float (input ('Comprimento do Cateto Oposto: '))
ca = float (input ('Comprimento do Cateto Adjacente: '))
hip = ((co ** 2) + (ca ** 2)) ** (1/2)
print ('A hipotenusa medirá {:.2f}'.format (hip))'''

'''import math
co = float (input ('Comprimento do Cateto Oposto: '))
ca = float (input ('Comprimento do Cateto Adjacente: '))
hip = math.hypot (co, ca)
print ('A hipotenusa medirá {:.2f}'.format (hip))'''

from math import hypot
co = float (input ('Comprimento do Cateto Oposto: '))
ca = float (input ('Comprimento do Cateto Adjacente: '))
hip = hypot (co, ca)
print ('A hipotenusa medirá {:.2f}'.format (hip))