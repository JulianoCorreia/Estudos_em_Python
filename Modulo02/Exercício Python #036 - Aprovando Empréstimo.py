'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
'''

print('===== DESAFIO 036   =====')

# Atribuições dos valores;
valorcasa = float(input('Informe o valor da casa: R$ '))
salario = float(input('Informe seu salário: R$ '))
anos = int(input('Anos para pagar a casa: '))

# Calcula o valor da prestação;
prestacao = valorcasa / (anos * 12)

# calcula se a prestação é superior a 30% do salário;
emprestimo = salario - (salario * 30 / 100)

print(f'O valor da prestação será de R$ {prestacao:.2f}')

if emprestimo > prestacao:
    print('Seu empréstimo foi APROVADO!')
else:
    print('Seu empréstimo foi NEGADO!')
