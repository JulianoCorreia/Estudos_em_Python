'''
 Faça um programa que leia um ângulo qualquer e mostre na tela o
 valor do seno, cosseno e tangente desse ângulo.
'''

print('=====   DESAFIO 018   =====')

from math import sin, cos, tan, radians

angulo = float(input('Digite o ângulo: '))
print(f'O ângulo de {angulo}º tem os valores: \n'
      f'SENO {sin(radians(angulo)):.2f}\n'
      f'COSSENO {cos(radians(angulo)):.2f}\n'
      f'TANGENTE {tan(radians(angulo)):.2f}')
