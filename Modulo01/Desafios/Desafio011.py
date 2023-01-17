#Faça um pograma que leia a largura  e a altura de uma
#parede em metros, calcule a sua área e a quantidade de tinta
#necessária para pintá-la, sabendo que cada litro de tinta
#pinta uma área de 2m².

print('=====   DESAFIO 011   =====')

larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
print(f'Largura {larg} x Altura {alt}\n'
      f'Sua parede tem {larg * alt:.2f}m²')
print(f"Você vai precisar de {(larg * alt) / 2 :.2f}l de tinta.")