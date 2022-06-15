# Refaça o exercício 35 dos triângulos, acrescentando o recurso de MOSTRAR QUE TIPO DE TRIÂNGULO será formado:
# EQUILÁTERO: todos os lados iguais
# ISÓSCELES: dois lados iguais
# ESCALENO: todos os lados diferentes

print ('=='*20)
print ('Analisador de Triângulos')
print ('=='*20)
reta_1 = float (input ('Primeiro segmento: '))
reta_2 = float (input ('Segundo segmento: '))
reta_3 = float (input ('Terceiro segmento: '))
if reta_1 < reta_2 + reta_3 and reta_2 < reta_1 + reta_3 and reta_3 < reta_1 + reta_2:
    print (' Os segmentos acima PODEM FORMAR UM TRIÂNGULO ', end='')
    if reta_1 == reta_2 == reta_3:
        print ('EQUILÁTERO')
    elif reta_1 != reta_2 != reta_3 != reta_1:
        print ('ESCALENO')
    else:
        print ('ISOSCÊLES')
else:
    print (' Os segmentos acima NÃO PODEM FORMAR UM TRIÂMGULO')
