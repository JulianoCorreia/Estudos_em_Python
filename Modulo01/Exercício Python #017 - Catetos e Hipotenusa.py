'''
Faça um programa que leia o comprimento do cateto oposto e
do cateto adjacente de um triângulo retângulo.
Calcule e mostre o comprimento da hipotenusa.
'''

from math import hypot

print('=====   DESAFIO 017   =====')
co = float(input('Cateto Oposto: '))
ca = float(input('Cateto Adjacente: '))
print(f'O valor da hipotenusa é: {hypot(co, ca):.2f}')
