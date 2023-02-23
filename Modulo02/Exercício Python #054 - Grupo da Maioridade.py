'''
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
'''

print('=====   DESAFIO 054   =====')

from datetime import date
ano_atual = date.today().year
maior_idade = 0
menor_idade = 0

for pessoas in range(1, 8):
    ano_nasc = int(input(f'Em que ano a {pessoas}º pessoa nasceu: '))
    idade = ano_atual - ano_nasc
    if idade >= 18:
        maior_idade += 1
    else:
        menor_idade += 1
print('')
print(f'Total de {menor_idade} pessoas menores de idade')
print(f'Total de {maior_idade} pessoas maiores de idade')