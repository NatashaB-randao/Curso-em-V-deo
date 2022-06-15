# Desenvolva um programa que leia O PRIMEIRO TERMO e a RAZÃO de uma PA (progressão aritmética)
# No final, mostre os 10 primeiros termos desta progressão

primeiro = int (input ('Primeiro termo: '))
razão = int (input ('Razão: '))
décimo = primeiro + (11-1) * razão
for c in range (primeiro, décimo, razão):
    print ('{}'.format (c), end= ' → ')
print ('ACABOU')

