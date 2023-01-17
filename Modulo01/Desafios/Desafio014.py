# Escreva um programa que converta uma temperatura
# digitando em graus Celsius e converta para graus Fahrenheit

print('=====   DESAFIO 014   =====')

c = float(input('Temperatura em ºC: '))
print(f'A temperatura de {c}ºC corresponde a:\n'
      f'{(9 * c / 5) + 32:.2f} ºF\n'
      f'{c + 273.15:.2f} K')