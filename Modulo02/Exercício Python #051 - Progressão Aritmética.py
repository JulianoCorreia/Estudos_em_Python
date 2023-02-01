'''
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
'''

print('=====   DESAFIO 051   =====')

print('=-='*7)
print(f'\033[7:31:40m 10 TERMOS DE UMA PA \033[m')
print('=-='*7)

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = termo + (11 - 1) * razao

for c in range (termo, decimo, razao):
    print(f'{c}', end=' -> ')
print('ACABOU')