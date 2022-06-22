"""

3.Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.


"""

sexo = input('Informe o sexo, apenas primeira letra: ')

if sexo == 'F':
    print(f'Feminino')
elif sexo == 'M':
    print(f'Masculino')
else:
    print('Sexo Inválido!.')
