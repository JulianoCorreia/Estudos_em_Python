'''
 Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
'''

print('=====   DESAFIO 046   =====')

from time import sleep

for num in range (10, -1, -1):
    sleep(0.5)
    print(num)
print('FELIZ ANO NOVO!')