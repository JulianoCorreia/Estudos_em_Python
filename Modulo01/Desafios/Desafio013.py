# Faça um algoritimo que leia o salário de um funcionário
# e mostre seu novo salario, com 15% de aumento.

print('=====   DESAFIO 013   =====')
s = float(input('Salário atual:R$ '))
a = float(input('Quantos % de aumento: '))
print(f'Novo salário com {a}% de aumento será: R$ {s + (s * a / 100):.2f}')