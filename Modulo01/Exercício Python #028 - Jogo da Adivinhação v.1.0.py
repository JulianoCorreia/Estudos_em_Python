'''
Escreva um programa que faça o computador "pensar" em um
número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''

print('=====   DESAFIO 028   =====')

# Importando biblioteca de escolha aleatória
from random import randint
from time import sleep

print('-=' * 28)
print('VOU PENSAR EM UM NÚMERO ENTRE 1 e 5. TENTE ADIVINHAR...')
print('-=' * 28)
n = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
# Jogador faz a escolha do noumero.
escolha = randint(1, 5)

if n == escolha:
    print('Parabéns!!! Você acertou.')
else:
    print(f'ERRROUUU !!!  Tente denovo... ha ha ha\n'
          f'Voce escolheu {n}, mas eu pensei no número {escolha}')
