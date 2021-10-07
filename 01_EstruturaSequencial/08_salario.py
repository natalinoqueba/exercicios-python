# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês
ganho = int(input('Quanto voce ganha por hora?\nR: '))
hora = int(input('Quantas horas voce trabalhou no mes?\nR: '))
salario = ganho * hora
print(f'O salario esse mes sera de {salario}Mt')
