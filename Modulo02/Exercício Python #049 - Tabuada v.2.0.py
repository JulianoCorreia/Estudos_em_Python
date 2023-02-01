'''
Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
'''

print('=====   DESAFIO 049   =====')

num = int(input('DIGITE O NÚMERO PARA VER SUA TABUADA: '))
cont = 0
for cont in range(1, 11):
    print(f'{num} x {cont:2} = {num * cont}')
