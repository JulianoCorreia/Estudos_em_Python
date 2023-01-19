'''
Crie um programa que leia um número inteiro e mostre na
tela se ele é PAR ou ÍMPAR.
'''
print('=====   DESAFIO 030   =====')
n = int(input('Digite um número: '))
resultado = n % 2
if resultado == 0:
    print(f'O número {n} é PAR.')
else:
    print(f'O número {n} é IMPAR.')
