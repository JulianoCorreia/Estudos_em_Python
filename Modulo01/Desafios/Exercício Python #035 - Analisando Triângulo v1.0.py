'''
Desenvolva um programa que leia o comprimento de três retas e
diga ao usuário se elas podem ou não formar um triângulo.
'''

from time import sleep
print('=====   DESAFIO 035   =====')
print(" ")

a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
print('Analisando o triângulo...')
sleep(2)

# A soma de dois lados não pode ser maior que o terceiro lado
if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima PODEM FORMAR um triângulo.')
else:
    print('Os segmentos acima NÃO PODEM um triângulo.')
