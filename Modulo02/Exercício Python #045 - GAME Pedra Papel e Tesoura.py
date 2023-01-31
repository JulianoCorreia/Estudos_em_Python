'''
Crie um programa que faça o computador jogar Jokenpô com você.
'''

print('=====   DESAFIO 045   =====')
print("")

from random import randint
from time import sleep
import emoji

print("")
print('[ 0 ] PEDRA ✊\n'
      '[ 1 ] PAPEL 🖐️\n'
      '[ 2 ] TESOURA ✌️')

#Lista de itens para escolha;
itens = ('PEDRA ✊', 'PAPEL 🖐️', 'TESOURA ✌️')

#Computador escolhe;
computador = randint(0, 2)

#Jogador escolhe;
jogador = int(input('QUAL SUA JOGADA? '))

print("")
if jogador >= 3:
    print('\033[7:41:46m JOGADA INVÁLIDA!\033[m')
    exit()

print('   JO')
sleep(0.5)
print('    KEN')
sleep(0.5)
print('   PO !')
sleep(0.5)

computador = randint(0, 2)
print("")
print('=-='*10)
print(f'JOGADOR ==> {itens[jogador]}')
print(f'COMPUTADOR ==> {itens[computador]}')
print('=-='*10)
print("")

#Computador PEDRA;
if computador == 0:

    #Jogador PEDRA;
    if jogador == 0:
        print('\033[0:36:32m EMPATOU \033[m')

    #Jogador PAPEL;
    elif jogador == 1:
        print('\033[0:31:40m JOGADOR VENCE \033[m')

    #Jogador TESOURA;
    elif jogador == 2:
        print('\033[0:37:40m COMPUTADOR VENCE \033[m')


#Computador PAPEL;
elif computador == 1:

    #Jogador PEDRA;
    if jogador == 0:
        print('\033[0:37:40m COMPUTADOR VENCE \033[m')

    #Jogador PAPEL;
    elif jogador == 1:
        print('\033[0:36:32m EMPATOU \033[m')

    #Jogador TESOURA;
    elif jogador ==2:
        print('\033[0:31:40m JOGADOR VENCE \033[m')


#Computador TESOURA;
elif computador == 2:

    #Jogador PEDRA;
    if jogador == 0:
        print('\033[0:31:40m JOGADOR VENCE \033[m')

    #Jogador PAPEL;
    elif jogador == 1:
        print('\033[0:37:40m COMPUTADOR VENCE \033[m')

    #Jogador TESOURA;
    elif jogador == 2:
        print('\033[0:36:32m EMPATOU \033[m')
