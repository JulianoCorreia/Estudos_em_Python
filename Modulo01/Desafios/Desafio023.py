'''
Faça um programa que leia um número de 0 a 9999 e mostre
na tela cada um dos dígitos separados.

Ex: Digite um número: 1834
unidade: 4
dezena: 3
centena: 8
milhar: 1
'''

print('=====   DESAFIO 023   =====')
n = int(input('Digite um número: '))
print('Analisando o número...')
print(f'Unidade: {n // 1 % 10}\n'
      f'Dezena: {n // 10 % 10}\n'
      f'Centena: {n // 100 % 10}\n'
      f'Milhar: {n // 1000 % 10}')
