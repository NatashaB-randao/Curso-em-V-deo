# Faça um programa que leia 3 números e mostre qual é o maior e qual é o menor

primeiro_número = float (input ('Digite o primeiro número: '))
segundo_número = float (input ('Digite o segundo número: '))
terceiro_número = float (input ('Digite o terceiro número: '))
# Verificando quem é o menor 
menor = primeiro_número
if segundo_número < primeiro_número and segundo_número < terceiro_número:
    menor = segundo_número
if terceiro_número < primeiro_número and terceiro_número < segundo_número:
    menor = terceiro_número
# Verificando quem é maior
maior = primeiro_número
if segundo_número > primeiro_número and segundo_número > terceiro_número:
    maior = segundo_número
if terceiro_número > primeiro_número and terceiro_número > segundo_número:
    maior = terceiro_número
print (' O menor número digitado foi {:.0f}'.format (menor))
print (' O maior número digitado foi {:.0f}'.format (maior))

