'''
Crie um programa que leia o nome de uma cidade diga
se ela começa ou não com o nome "SANTO".
'''

print('=====   DESAFIO 024   =====')

cidade = str(input('Informe a cidade: ')).strip().capitalize()
print(cidade[:5] == 'Santo')
