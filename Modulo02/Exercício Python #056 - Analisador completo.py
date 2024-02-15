'''
Desenvolva um programa que leia o nome, 
idade e sexo de 4 pessoas.
No final do programa, mostre:
- a média de idade do grupo;
- qual é o nome do homem mais velho;
- quantas mulheres têm menos de 20 anos.
'''

print('=====   DESAFIO 056   =====')
print('')

total_mulheres = 0
homem_maior_idade = 0
nome_mais_velho = 0
soma_idade = 0

for pessoa in range(1, 5):
    print(f'--- {pessoa}º PESSOA ---')
    nome = str(input('Nome: ')).strip() .capitalize()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    soma_idade += idade

    if pessoa == 1 and sexo in 'Mm':
        homem_maior_idade = idade
        nome_mais_velho = nome
    if sexo in 'Mm' and idade > homem_maior_idade:
        homem_maior_idade = idade
        nome_mais_velho = nome
    if sexo in 'Ff' and idade < 20:
        total_mulheres += 1
print('')
media = soma_idade / 4
print(f'A idade média do grupoe é: {media:.1f} anos')
print(f'O homem mais velho tem {homem_maior_idade} anos e se chama {nome_mais_velho}')
print(f'Ao todo temos {total_mulheres} mulheres com menos de 20 anos.')
