# Faça um algoritimo que leia o preço de um produto e mostre
# seu novo preço, com 5% de desconto.

print('=====   DESAFIO 012   =====')

preco = float(input('Valor do produto:R$ '))
desc = float(input('Quantos % sera o desconto: '))
print(f"O seu desconto: R${preco * desc / 100:.2f}")
print(f'O valor com o desconto será de R${preco - (preco * desc / 100):.2f}')
