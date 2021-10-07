# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o
# total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e
# 5% para o sindicato, faça um programa que nos dê:
from time import sleep

ganho = int(input('Quanto voce ganha por hora?\nR: '))
hora = int(input('Quantas horas voce trabalhou no mes?\nR: '))
salario = ganho * hora  # a. salário bruto.
inss = (salario * 8) / 100  # b. quanto pagou ao INSS.
sind = (salario * 5) / 100  # c. quanto pagou ao sindicato.
ir = (salario * 11) / 100  # quanto tirou para o imposto de rendaz
desconto = inss + sind + ir
salario_liquido = salario - desconto  # e. o salário líquido.
print(
    f'\n+ Salario Bruto : {salario}MT \n- Imposto de Renda (11%) :{ir}MT \n- INSS (8%) : {inss} \n- Sindicato (5%) : {sind}MT \n= Salario Liquido : {salario_liquido}MT')
sleep(10)
