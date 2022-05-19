"""

11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
    a. o produto do dobro do primeiro com metade do segundo .
    b. a soma do triplo do primeiro com o terceiro.
    c. o terceiro elevado ao cubo.
"""
import math

n1 = int(input('Informe um numero inteiro: '))

n2 = int(input('Informe outro numero inteiro: '))

nR = float(input('Informe um numero real: '))

a = n1 * 2 * (n2 / 2)

b = n1 * 3 + nR

c = nR**3

print(f'Resultado de a: {a}, b: {b}, c: {c}')





