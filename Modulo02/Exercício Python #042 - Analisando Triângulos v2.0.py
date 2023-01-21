'''
 Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes
'''

print('=====   DESAFIO 042   =====')
print(" ")

# Coletando informações do triângulo.
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
print(" ")

#Testando se é triângulo;
if a < b + c and b < a + c and c < b + a:
    print('Os segmentos podem formar um triângulo ', end='')

#TRIÂNGULO EQUILÁTERO;
    if a == b == c:
        print('EQUILÁTERO.')

# TRIÂNGULO ISÓSCELES;
    elif a == b or a == c or c == b:
        print('ISÓSCELES.')

# Triângulo ESCALENO;
    elif a != b != c != a:
        print('ESCALENO.')

# Não formam triângulo;
else:
    print('Os segmentos NÃO PODEM FORMAR um triângulo.')
