'''
 Faça um programa que leia uma frase pelo teclado e mostre
 quantas vezes aparece a letra "A", em que posição ela aparece a
 primeira vez e em que posição ela aparece a última vez.
'''

print('=====   DESAFIO 026   =====')
frase = str(input('Digite a letra para Analisar: ')).strip().upper()
l = str(input('Qual letra quer analisar? ')).strip().upper()
print(f'Analisando a letra "{l}"...')
print(f'A letra "{l}" aparece {frase.count(l)} vezes.\n'
      f'A letra "{l}" aparece primeiro na posição {frase.find(l) + 1}".\n'
      f'A letra "{l}" aparece a última vez na posição {frase.rfind(l) + 1}')
