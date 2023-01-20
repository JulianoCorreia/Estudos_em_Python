# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

print('=====   DESAFIO 004   =====')
n = input('Digite algo: ')
print('O tipo primitivo é', type(n))
print('So tem espaços? ', n.isspace())
print('É maiúsculo? ', n.isupper())
print('É alfabético? ', n.isalpha())
print('É minúsculo? ', n.islower())
print('Está capitalizada? ', n.istitle())
print('É alfanumérico? ', n.isalnum())
