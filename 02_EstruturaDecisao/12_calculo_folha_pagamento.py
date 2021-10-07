valor_hora = float(input('Quanto recebe por hora?\nR: '))
horas_trabalhadas = float(input('Quantas horas trabalhou no presente mes?\nR: '))
salario_bruto = valor_hora * horas_trabalhadas
salario_liquido = 0
inss = 0
ir = 0
fgts = 0
descontos = 0
if salario_bruto <= 900:
    ir = 0
    inss = 0.1 * salario_bruto
    fgts = 0.11 * salario_bruto
    descontos = ir + inss
    salario_liquido = salario_bruto - descontos
elif salario_bruto <= 1500:
    ir = 0.05 * salario_bruto
    inss = 0.1 * salario_bruto
    fgts = 0.11 * salario_bruto
    descontos = ir + inss
    salario_liquido = salario_bruto - descontos
elif salario_bruto <= 2500:
    ir = 0.1 * salario_bruto
    inss = 0.1 * salario_bruto
    fgts = 0.11 * salario_bruto
    descontos = ir + inss
    salario_liquido = salario_bruto - descontos
elif salario_bruto > 2500:
    ir = 0.2 * salario_bruto
    inss = 0.1 * salario_bruto
    fgts = 0.11 * salario_bruto
    descontos = ir + inss
    salario_liquido = salario_bruto - descontos
print(f'Salario Bruto: ({valor_hora} * {horas_trabalhadas}) : Mt {salario_bruto}')
print(f'(-) IR (5%)  :Mt {ir}')
print(f'(-) INSS (10%)  : Mt {inss}')
print(f'FGTS (11%)  : Mt {fgts}')
print(f'Total de descontos  : Mt {descontos}')
print(f'Salario Liquido  : Mt {salario_liquido}')
