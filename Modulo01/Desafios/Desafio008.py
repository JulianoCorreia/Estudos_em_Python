# Escreva um programa que leia um valor em metros e o exiba
# convertido em centímetros e milímetros.

print('=====   DESAFIO 008   =====')

m = float(input('Distância em metros: '))
print(f'{m:.0f} metro(s) corresponde a: \n'
      f'{m*1000} Quilômetros \n'
      f'{m / 100} Hectometros \n'
      f'{m / 10:.0f} Decametros \n'
      f'{m * 10:.0f} Decimetros \n'
      f'{m*100:.0f} Centímetros \n'
      f'{m*1000:.0f} Milimetros \n')
