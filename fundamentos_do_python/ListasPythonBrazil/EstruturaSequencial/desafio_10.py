"""

10. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

"""

import math

C = float(input('Informe a temperatura em graus Celsius: '))

F = (C * 1.8) + 32

print(f'Temperatura em graus Fahrenheit: {math.floor(F)}')
  

