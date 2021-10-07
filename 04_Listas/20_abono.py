salarios = list()
abonos = list()
funcioarios = total_abono = funcionario_menor = maior_abono = 0
print('Projeção de Gastos com Abono'
      '='*15)
while True:
    salario = int(input('Salario: '))
    if salario == 0:
        break
    salarios.append(salario)
    abono = salario * 0.2
    if abono <= 100:
        abono = 100
        funcionario_menor += 1
    abonos.append(abono)
    funcioarios += 1
    total_abono += abono
    if abono > maior_abono:
        maior_abono = abono
print('\n\nSalario      - Abono')
for x, salario in enumerate(salarios):
    print(f'MT Salario: {salario:4} - MT {abonos[x]:.5f}')
print(f'\nForam processados {funcioarios} colaboradores'
      f'\nTotal gasto com abonos: {total_abono}'
      f'\nValor mínimo pago a {funcionario_menor} colaboradores'
      f'\nMaior valor de abono pago: {maior_abono}')