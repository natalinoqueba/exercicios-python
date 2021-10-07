def validar(cpf):
    soma = som = 0
    val = False
    p = (10, 9, 8, 7, 6, 5, 4, 3, 2)
    p2 = (11, 10, 9, 8, 7, 6, 5, 4, 3)
    cpf = cpf.replace('.', '')
    cpf = cpf.split('-')
    for x in range(len(cpf[0]) - 1, -1, -1):
        soma += int(cpf[0][x]) * int(p[x])
    div = soma * 10 % 11
    if div == 10:
        div = 0
    for x in range(len(cpf[0]) - 1, -1, -1):
        som += int(cpf[0][x]) * int(p2[x])
    som += int(cpf[1][0]) * 2
    dv = som * 10 % 11
    if div == int(cpf[1][0]) and int(cpf[1][1]) == dv:
        for x in range(1, 10):
            if cpf[0].count(str(x)) == 9 and cpf[1].count(str(x)) == 2:
                val = False
                break
            else:
                val = True
    return val


valido = validar(input('CPF: '))
if valido:
    print('CPF valido')
else:
    print('CPF invalido')
