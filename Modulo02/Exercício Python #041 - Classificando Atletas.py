'''
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER
'''

print('=====   DESAFIO 041   =====')
print(" ")

# Importa módulo para busca do ano
from datetime import date

# Busca ano do sistema
ano_atual = date.today().year

ano_nasc = int(input('Informe o ano de nascimento: '))
idade = ano_atual - ano_nasc

print(f'O atleta tem {idade} anos.')
# MIRIM
if idade <= 9:
    print('Categoria MIRIM')

# INFANTIL
elif idade <= 14:
    print('Categoria INFANTIL')

# JÚNIOR
elif idade <=19:
    print('Categoria JÚNIOR')

# SÊNIOR
elif idade <= 25:
    print('Categoria SÊNIOR.')

# MASTER
else:
    print('Categoria MASTER')
