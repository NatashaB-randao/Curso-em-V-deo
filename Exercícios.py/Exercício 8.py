# ==== Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros ====
metros = float (input('Digite um valor: '))
centímetros = int (metros*100)
milímetros = int (metros*1000)
print ('{} metros é equivalente à {:.1f} centímetros e {:.1f} milímetros'.format(metros, centímetros, milímetros))
