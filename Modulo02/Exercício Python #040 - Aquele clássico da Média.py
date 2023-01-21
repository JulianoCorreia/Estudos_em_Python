'''
 Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO
'''

print('=====   DESAFIO 040   =====')

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2

# REPROVADO;
if media < 5.0:
    print(f'Média {media:.1f} Aluno REPROVADO!')

# RECUPERAÇÃO;
elif media >= 5.0 and media <= 6.9:
    print(f'Média {media:.1f} Você está em RECUPERAÇÃO')

# APROVADO;
else:
    media > 7.0
    print(f'Média {media:.1f} Parabéns, você foi APROVADO!')
