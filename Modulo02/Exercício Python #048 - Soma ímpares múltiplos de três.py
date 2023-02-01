'''
Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
'''

print('=====   DESAFIO 048   =====')

soma = 0
cont = 0
for num in range(1, 501, 2):
    if num % 3 == 0:

        #Aqui conta quando encontra o numero correspondente
        cont = cont + 1

        #Aqui soma o valor do número que foi encontrado acima
        soma = soma + num

print(f'Foram encontrados {cont} valores.\n'
      f'A soma de todos eles é: {soma}')