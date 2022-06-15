# Faça um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo"
cidade = str (input ('Em qual cidade você nasceu? ')).strip()
print (cidade [0:5].upper() == 'SANTO')
