'''
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele
foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
'''

print('=====   DESAFIO 029   =====')

v = float(input('Qual a velociade atual do carro? '))

if v > 80:
    multa = (v - 80) * 7
    print(f'MULTADO! Você excedeu o limite de velocidade permitido de 80km/h\n'
          f'Você deve pagar uma multa de R${multa:.2f}!')
print('Muito bem! Boa viagem')
