'''
Escreva um programa que pergunte o salário de um funcionário e
calcule o valor do seu aumento. Para salários superiores a R$1250,00,
calcule um aumento de 10%. Para inferiores ou iguais, o aumento é de 15%.
'''

print('=====   DESAFIO 034   =====')
salario = float(input('Informe o salário:R$ '))
print(" ")

if salario > 1250:  # Ajuste de 10%
    ajuste = salario + (salario * 10 / 100)
    print('Reajuste de 10%')

else:  # Ajuste de 15%
    ajuste = salario + (salario * 15 / 100)
    print('Reajuste de 15%')

print(f'Seu novo salário: R$ {ajuste:.2f}')
