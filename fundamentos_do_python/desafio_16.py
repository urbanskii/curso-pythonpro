"""

16.Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
   Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam
   R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

"""

metros = float(input('Informe o tamanho em metros quadrados da área a ser pintada: '))
litros = metros/3

preco_litro = 80.0
capacidade_litro = 18

latas = litros / capacidade_litro
total = latas * preco_litro

print('Você usara: {:.2f} latas de tinta'.format(latas))
print('O preço total é de R${:.2f}'.format(total))

