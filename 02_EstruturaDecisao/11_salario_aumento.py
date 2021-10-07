# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes...
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5%
#Após o aumento ser realizado, informe na tela:
# salário antes do reajuste;
# percentual de aumento aplicado;
# valor do aumento;
# novo salário, após o aumento

aumento = 0
salario = float(input('Salario do colaborador: '))
if salario <= 280:
    aumento = salario * 0.2
elif 280 < salario < 700:
    aumento = salario * 0.15
elif 700 <= salario < 1500:
    aumento = salario * 0.1
elif salario >= 1500:
    aumento = salario * 0.05
salario_aumento = salario + aumento
print('\n\n=====================================')
print(f'Salario antes do reajuste: {salario}')
if salario <= 280:
    print('Percentual de aumento aplicado: 20%')
elif 280 < salario < 700:
    print('Percentual de aumento aplicado: 15%')
elif 700 <= salario < 1500:
    print('Percentual de aumento aplicado: 10%')
elif salario >= 1500:
    print('Percentual de aumento aplicado: 5%')
print(f'Valor do aumento: {aumento}')
print(f'Salario apos aumento: {salario_aumento}')
print('=====================================')
