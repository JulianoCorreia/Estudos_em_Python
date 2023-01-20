'''
Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
1 para binário, 2 para octal e 3 para hexadecimal.
'''
print('=====   DESAFIO 037   =====')

numero = int(input('Digite um número inteiro: '))

#Seleciona a base
print('[ 1 ] BINÁRIO\n'
      '[ 2 ] OCTAL\n'
      '[ 3 ] HEXADECIMAL')
escolha = int(input('Escolha uma base para conversão: '))

# Converte para BINáRIO;
if escolha == 1:
    print(f'O número {numero}, convertido para BINÁRIO é {format(numero, "b")}')

# Converte para OCTAL;
elif escolha == 2:
    print(f'O número {numero}, convertido para OCTAL É {format(numero, "o")}')

# Converte para HEXADECIMAL;
elif escolha == 3:
    print(f'O número {numero}, convertido para HEXADECIMAL é {format(numero, "x")}')
else:
    print('Opção inválida. Tente novamente.')