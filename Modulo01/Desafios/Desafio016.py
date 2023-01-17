'''
Crie um programa que leia um número Real qualquer pelo
teclado e mostre na tela a sua porção Inteira.
'''

print('=====   DESAFIO 016   =====')

from math import trunc

num = float(input('Digite um valor: '))
print(f'O número {num} tem o valor de sua porção inteira: {trunc(num)}')
