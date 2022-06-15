# === Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m­^2 ===
largura = float (input ('Digite o valor da largura da parede: '))
altura = float (input ('Digite o valor da altura da parede: '))
área = float (largura*altura)
print (' A parede tem a dimensão de {} x {} e sua área é de {} m²'.format(largura, altura, área))
tinta = float (área / 2)
print (' Para pintar a parede, você precisará de {}l de tinta'.format(tinta))
