'''
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
desconsiderando os espaços.
ex:
apos a sopa
a sacada da casa
o lobo ama o bolo
'''

print('=====   DESAFIO 053   =====')

frase = str(input('Digite uma frase: ')).strip() .upper()
palavras = frase.split() #Retira o espaço no início e final da frase
junto = ''.join(palavras) #Elimina os espaços internos entre as palavras
inverso = ''
for letra in range(len(junto)-1,-1,-1):
    inverso += junto[letra]
if inverso == junto:
    print('Temos um PALÍNDROMO!')
else:
    print('A frase não é um palíndromo.')


