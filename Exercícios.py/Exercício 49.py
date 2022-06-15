# Refaça o desafio 9, mostrando a TABUADA de um número que o usuário escolher
# Só que agora utilizando um laço de repetição 


tabuada = int (input ('Qual tabuada você quer que eu resolva? '))
for c in range (1,11):
    resultado = (tabuada * c)
    print ('{} x {:.0f} = {}'.format (tabuada, c, resultado))
