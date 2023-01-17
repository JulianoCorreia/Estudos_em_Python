'''
Faça um programa que leia três números e mostre
qual é o MAIOR e qual é o MENOR.
'''

print('=====   DESAFIO 033   =====')

print('*** MAIOR e MENOR ***')
a = int(input('1º número: '))
b = int(input('2º número: '))
c = int(input('3º número: '))
print(" ")
# Encontrando o número menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print(f'O menor número digitado: {menor}')

# Encontrando o número maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'O maior número digitado: {maior}')
