'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros
'''

print('=====   DESAFIO 044   =====')

preco = float(input('Valor da compra R$: '))

print('\033[0:33:7m=-=-=-= FORMA DE PAGAMENTO =-=-=-=\033[m')
print("")
print('[ 1 ] À VISTA DINHEIRO - DESCONTO DE 10% \n'
      '[ 2 ] À VISTA CARTÃO - DESCONTO DE 5%\n'
      '[ 3 ] ATÉ 2x NO CARTÃO SEM JUROS\n'
      '[ 4 ] 3x OU + NO CARTÃO COM JUROS')
print("")
pagamento = int(input('ESCOLHA A FORMA DE PAGAMENTO: '))
print("")
if pagamento == 1:
    dinheiro = preco - (preco * 10 / 100)
    print('Valor com 10% de desconto.')
    print(f'Total da compra: R$ {dinheiro:.2f}')

elif pagamento == 2:
    cartao = preco - (preco * 5 / 100)
    print('Valor com 5% de desconto no cartão.')
    print(f'Total da compra: R$ {cartao:.2f}')

elif pagamento == 3:
        num_parcelas = preco / 2
        print(f'Sua compra de R$ {preco:.2f}, será parcelada em 2x de R$ {num_parcelas:.2f} SEM JUROS')
        print(f'Valor total da compra: R$ {preco:.2f}')

elif pagamento == 4:
        num_parcelas = int(input('Quantas parcelas: '))
        print("")
        if num_parcelas <= 2:
            parcelas = preco / num_parcelas
            print(f'Sua compra de R$ {preco:.2f}, será parcelada em {num_parcelas}x de R$ {parcelas:.2F} SEM JUROS')
            print(f'Valor total da compra: R$ {preco:.2f}')

        elif num_parcelas >= 3:
            juros_cartao = preco + (preco * 20 / 100)
            parcelas = juros_cartao / num_parcelas
            print(f'Sua compra de R$ {preco:.2f}, será parcelada em {num_parcelas}x de R$ {parcelas:.2f}')
            print(f'Valor total da compra com JUROS: R$ {juros_cartao:.2f}')
else:
    print('\033[0:31:40m !!! FORMA DE PAGAMENTO INVÁLIDA !!!\033[m')
