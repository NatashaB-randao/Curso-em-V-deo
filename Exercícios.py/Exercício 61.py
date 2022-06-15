# Refaça o desafio '51', lendo o PRIMEIRO TERMO e a RAZÃO de uma PA. 
# Mostrando os 10 PRIMEIROS TERMOS da progressão usando estrutura WHILE. 

print (' GERADOR DE PA  ')
print ('-=' * 10)
primeiro = int (input ('Primeiro termo: '))
razão = int (input ('Razão: '))
termo = primeiro
contador = 1

while contador <= 10:
    print ('{} '.format (termo), end= ' → ')
    termo = (termo + razão)
    contador = (contador + 1)
print ('FIM')

