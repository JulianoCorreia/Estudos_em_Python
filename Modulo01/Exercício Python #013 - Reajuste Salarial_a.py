# Crie um programa que leia o valor de um produto e
# mostre o desconto no pagamento a vista e o acréscimo
# no pagamento a prazo.

('===== DESAFIO 013b   =====')
preco = float(input('Valor do produto:R$ '))
#a vista
d = preco - (preco * 10 / 100)

#a prazo
a = preco + (preco * 8 / 100)
print('== Valor a vista ==')

print(f'A vista com 10% de desconto:R$ {d:.2f}\n'
      f'O valor do desconto:R$ {preco * 10 / 100:.2f}\n')

print('== Valor a prazo ==')
print(f'A prazo com acréscimo de 8%: R$ {a:.2f} \n'
      f'O valor do acréscimo: R$ {preco * 8 / 100:.2f}')

