'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''

print('=====   DESAFIO 039   =====')

# Importando modulo para buscar ano atual da maquina;
from datetime import date

ano_nasc = int(input('Informe o ano de nascimento: '))
print(" ")

#Buscando ano atual na maquina;
ano_atual = date.today().year

# Calulando idade;
idade = ano_atual - ano_nasc

if idade == 18: #Exatos 18 anos de idade;
    print(f'Você tem {idade} anos de idade em {ano_atual}.\n'
          f'Apresente-se no centro de recrutamento militar')

elif idade > 18: #Maiores de 18 anos de idade;
    print(f'Você nasceu em {ano_nasc}, você tem {idade} anos soldado!\n'
          f'Está {idade - 18} atrasado com seu alistamento militar.')
    print(f'Deveria ter sido feito em {ano_nasc + 18}.!')

else: #Menores de 18 anos de idade;
    print(f'Você nasceu em {ano_nasc}, tem {idade} anos em {ano_atual}.\n'
          f'Ainda faltam {idade - 18} anos para o seu alistamento militar.')