# Crie um programa que leia uma FRASE qualquer e diga se ela é um PALÍNDROMO, desconsiderando os espaços


frase = str (input ('Digite uma frase: ')).strip().upper()      #elimina os espaços do início e final e joga tudo para maiúscula
palavras = frase.split()        #separa a frase em uma lista (coleção)
junto = ''.join(palavras)       #junta as palavras desconsiderando os espaços
#inverso = ''
inverso = junto [::-1]
'''for letra in range(len(junto) - 1, -1, -1):
    inverso = inverso + junto [letra]'''
print ('O inverso de {} é {}'.format (junto, inverso))
if inverso == junto:
    print ('Temos um PALÍMDROMO')
else:
    print ('A frase NÃO É UM PALÍNDROMO')
