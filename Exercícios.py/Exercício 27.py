# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente
# Ex.: Ana Maria de Souza
# Primeiro = Ana
# Segundo = Souza

nome = str (input ('Digite o seu nome completo: ')).strip()
n = nome.split()
print ('Prazer em te conhecer!')
print ('O seu primeiro nome é: {}'.format (n [0]))
print ('O seu último nome é: {}'.format (nome [len (n)-1]))
