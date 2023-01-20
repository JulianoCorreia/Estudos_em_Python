# Escreva um programa que pergunte a quantidade de Km
# percorridos por um carro alugado e a quantidade de dias
# pelos quais ele foi alugado. Calcule o preço a pagar, sabendo
# que o carro custa R$60 por dia e R$0,15 por Km rodado.

print('=====   DESAFIO 015   =====')

dias = int(input('Dias alugados: '))
km = float(input('Km rodados: '))
print(f'Você deverá pagar:R$ {(dias * 60) + (km * 0.15):.2f}')
