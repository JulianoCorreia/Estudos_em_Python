#Crie um programa que leia quanto dinheiro uma pessoa tem na
#carteira e mostre quantos Dólares e Euros ela pode comprar.
#Dólar = 5.29
#Euro = 5.67
print('=====   DESAFIO 010   =====')

n = float(input('Quanto dinheiro você tem:R$ '))
print(f'Você pode comprar: \n'
      f'U$${n * 3.27:.2f} dólares\n'
      f'€{n * 5.67:.2f} euros')