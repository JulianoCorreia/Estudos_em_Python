'''
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km
para viagens de até 200Km e R$0,45 parta viagens mais longas.
'''

print('=====   DESAFIO 031   =====')

distancia = float(input('Distância em Km da viagem: '))
if distancia > 200:
    # Viagens longas
    passagem = distancia * 0.45
else:
    # Preço normal
    passagem = distancia * 0.50

print(f'Valor da passagem: R${passagem:.2f}')
print('*** Boa Viagem ***')

'''
if inline (modo simplificado)
distancia = float(input('Distância em Km da viagem: '))
passagem = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print(f'Valor da passagem {passagem:.2f}\n'
      f'*** Boa Viagem ***')
'''
