# crie uma TUPLA preenchida com os 20 PRIMEIROS colocados da Tabela do Campeonado Brasileiro de Futebol na ordem de colocação
# depois mostre:
# a) Apenas os 5 primeiros colocados
# b) Os 4 últimos colocados da tabela
# b) Uma lista com os times na ordem alfabética
# d) Em que posição da tabela está a Chapecoense

times = ('Atlético-MG', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Bragantino', 
'Corinthians', 'Internacional', 'Fluminense', 'Cuiabá', 'Athletico-PR',
'Atlético-GO', 'São Paulo', 'Ceará', 'Santos', 'Bahia', 
'Juventude', 'Grêmio', 'América-MG', 'Sport', 'Chapecoense')
print ('-='*30)
for t in times:
    print (t)
#print (f'Lista de times do Brasileirão: {times}')
print ('-='*30)
print (f'Os 5 primeiros colocados são: {times[0:5]}')
print ('-='*30)
print (f'Os 4 últimos colocados são: {times[-4:]}')
print ('-='*30)
print (f'Times em ordem alfabética: {sorted(times)}')
print ('-='*30)
print (f'O Chapecoense está na {times.index("Chapecoense")+1}ª posição')
print ('-='*30)
