'''
 Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.
'''

print('=====   DESAFIO 022   =====')

nome = str(input('Seu nome completo: ')).strip()
letras = len(nome) - nome.count(' ')
primeironome = nome.find(' ')

# Maiúsculas
print(f'Seu nome em maiúsculas: {nome.upper()}')

# Minúsculas
print(f'Seu nome em minúsculas: {nome.lower()}')

# Quantas letras sem contar os espaços.
print(f'Seu nome tem ao todo {letras} letras')

# Quantas letras tem o primeiro nome
print(f'Seu primeiro nome tem {primeironome} letras')
