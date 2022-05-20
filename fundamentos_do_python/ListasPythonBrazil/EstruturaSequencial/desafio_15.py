"""

15.Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do
   seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato,
   faça um programa que nos dê:

        a. salário bruto.
        b. quanto pagou ao INSS.
        c. quanto pagou ao sindicato.
        d. o salário líquido.
        e. calcule os descontos e o salário líquido, conforme a tabela abaixo:
            
            + Salário Bruto : R$
            - IR (11%) : R$
            - INSS (8%) : R$
            - Sindicato ( 5%) : R$
            = Salário Liquido : R$

            Obs.: Salário Bruto - Descontos = Salário Líquido.

"""

hora_trabalhada = float(input('Informe valor ganho por hora: '))
qtd_horas_trabalhadas  = float(input('Informe o número de horas trabalhadas no mês: '))

salario_bruto = hora_trabalhada * qtd_horas_trabalhadas
ir = salario_bruto - (salario_bruto - (salario_bruto * 0.11))
inss = salario_bruto - (salario_bruto - ( salario_bruto * 0.08))
sindicato = salario_bruto - (salario_bruto - (salario_bruto * 0.05))
salario_liquido = salario_bruto - ir - inss - sindicato



print('+ Salário Bruto : R$ {:.2f}'.format(salario_bruto))
print('- IR (11%) : R$ {:.2f}'.format(ir))
print('- INSS (8%) : R$ {:.2f}'.format(inss))
print('- Sindicato ( 5%) : R$ {:.2f}'.format(sindicato))
print('= Salário Liquido : R$ {:.2f}'.format(salario_liquido))
