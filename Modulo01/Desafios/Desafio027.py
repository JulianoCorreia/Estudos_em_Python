'''
Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente.
'''

print('=====   DESAFIO 027   =====')
n = str(input('Seu nome completo: ')).strip().title()
nome = n.split()
print(f'Olá! Muito prazer {n}\n'
      f'Seu primeiro nome é: {nome[0]}\n'
      f'Seu último nome é: {nome[len(nome) - 1]}')
