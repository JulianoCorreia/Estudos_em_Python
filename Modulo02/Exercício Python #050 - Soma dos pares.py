'''
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
'''

print('=====   DESAFIO 050   =====')

pares = 0
impares = 0
parcont = 0
imparcont = 0
for n in range (1, 7):
    n = int(input(f'Digite o {n}º número: '))

    #Somando PARES;
    if n % 2 == 0:
        pares = pares + n
        parcont += 1

    #Somando IMPARES;
    else:
        impares = impares + n
        imparcont += 1
print("")
print(f'Você digitou {parcont} números PARES. A soma deles é: {pares}\n'
      f'Você digitou {imparcont} números ÍMPARES. A soma deles é: {impares}')
