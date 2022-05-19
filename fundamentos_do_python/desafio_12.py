"""

12. Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: 
    (72.7*altura) - 58

"""
import math

altura = float(input('Informe a altura: '))

peso_ideal = (72.7*altura) - 58

print(f'Peso ideal para a altura informada: {math.floor(peso_ideal)}')


