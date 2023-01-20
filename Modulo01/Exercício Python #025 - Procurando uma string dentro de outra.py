'''
Crie um programa que leia o nome de uma pessoa e
diga se ela tem "SILVA" no nome.
'''

print('=====   DESAFIO 025   =====')
nome = str(input('Qual seu nome completo: ')).strip()
teste = 'SILVA' in nome.upper().split()
print(f'Seu nome tem Silva? {teste}')
