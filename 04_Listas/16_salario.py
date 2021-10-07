salario = list()
sal = (200, 300, 400, 500, 600, 700, 800, 900)
vals = valsemana = nr = ml = 0
while True:
    vals = int(input('Quanto o vendedor fez nessa semana?: '))
    if vals == 0:
        break
    valsemana = 200 + vals * 0.09
    salario.append(valsemana)
print('\n\n')
print(salario)
for x in sal:
    nr = ml = 0
    for y in salario:
        if x+99 >= y >= x:
            nr += 1
        elif y >= 1000:
            ml += 1
    print(f'Numero de vendedores com salarios no intervalo de {x} a {x + 99}: {nr}')
print(f'Numero de vendedores com salarios no intervalo de 1000 em diante: {ml}')