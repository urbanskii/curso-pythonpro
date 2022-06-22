"""


5. Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
        A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
        A mensagem "Reprovado", se a média for menor do que sete;
        A mensagem "Aprovado com Distinção", se a média for igual a dez.


"""

nota_01 = float(input('Informe a primeira nota: '))
nota_02 = float(input('Informe a segunda nota: '))

media = (nota_01 + nota_02) / 2

if media >= 70 and media < 100:
    print(f'Aprovado! media: {media}')
elif media < 70:
    print(f'Reprovado! media: {media}')
elif media == 100:
    print(f'Aprovado com distinção')
