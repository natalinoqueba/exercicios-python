aumento = 1.5
salario = float(input('Salario inicial: '))
for ano in range(1996, 2015):
    print(f' {ano} {aumento:.2f} {salario:.2f}')
    salario += salario * (aumento / 100)
    aumento *= 2
print(f'salario atual: {salario:.2f}')