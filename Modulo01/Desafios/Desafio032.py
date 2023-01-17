'''
Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
'''

print('=====   DESAFIO 032   =====')

# importa módulo para trabalhar com datas.
from datetime import date

ano = int(input('Qual ano você quer analisar?\n'
                'Informe o ano ou digite 0 para o ano atual: '))
if ano == 0:
    ano = date.today().year  # Busca o ano configurado na maquina

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano de {ano} é BISSEXTO.')
else:
    print(f'O ano de {ano} não é BISSEXTO.')
