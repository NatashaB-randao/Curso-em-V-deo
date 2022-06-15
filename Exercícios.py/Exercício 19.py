# === Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido ===
import random
primeiro_aluno = input ('Primeiro aluno: ')
segundo_aluno = input ('Segundo aluno: ')
terceiro_aluno = input ('Terceiro aluno: ')
quarto_aluno = input ('Quarto aluno: ')
lista = [primeiro_aluno, segundo_aluno, terceiro_aluno, quarto_aluno] 
escolhido = random.choice (lista)
print ('O aluno escolhido foi {}'.format (escolhido))
