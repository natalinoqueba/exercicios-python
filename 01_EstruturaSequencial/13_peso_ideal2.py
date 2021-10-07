# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# utilizando as seguintes fórmulas: Para homens: (72.7*h) - 58

altura = float(input('Qual e a sua altura em metros?\nR: '))
pideal = (72.7*altura)-58
print(f'Peso ideal para homens essa altura e {pideal}kg')
# Para mulheres: (62.1*h) - 44.7
pmideal = (62.1*altura)-47.7

print(f'Peso ideal para mulheres com essa altura e {pmideal}kg')
