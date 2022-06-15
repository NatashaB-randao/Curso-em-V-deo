# === O mesmo professor quer sortear a ordem a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada. ===
import random
primeiro = input ('Primeiro aluno: ')
segundo = input ('Segundo aluno: ')
terceiro = input ('Terceiro aluno: ')
quarto = input ('Quarto aluno: ')
lista = [primeiro, segundo, terceiro, quarto]
random.shuffle (lista)
print ('A ordem de apresentação será')
print (lista)
