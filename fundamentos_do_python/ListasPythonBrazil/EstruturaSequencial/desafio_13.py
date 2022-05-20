"""

13.Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes
fórmulas:
    a. Para homens: (72.7*h) - 58
    b. Para mulheres: (62.1*h) - 44.7

"""
import math

h = float(input('Informe a altura: '))
s = input('Informe o sexo "M para Masculino e F para Feminino": ')

a = (72.7*h) - 58

b = (62.1*h) - 47

if s == 'M':
    print(f'Peso ideal: {math.floor(a)}')
elif s == 'F':
    print(f'Peso ideal: {math.floor(b)}')
else:
    print('Informe o sexo corretamente!')


