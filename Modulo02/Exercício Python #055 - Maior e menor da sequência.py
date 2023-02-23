'''
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
'''

print('=====   DESAFIO 055   =====')

maior_peso= 0
menor_peso = 0

for p in range(1, 6):
    peso = float(input(f'Informe o {p}º peso Kg: '))
    if p == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if menor_peso > peso:
            menor_peso = peso
print('')
print(f'O maior peso foi {maior_peso} Kg.')
print(f'O menor peso foi {menor_peso} Kg.')
