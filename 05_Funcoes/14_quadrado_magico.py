def quadrado_magico(n=''):
    quadrado = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    linha = list()
    for x in quadrado:
        for y in quadrado:
            for z in quadrado:
                soma = x + y + z
                if soma == 15:
                    linha_1 = [x, y, z]
                    linha.append(linha_1[:])
    for x in range(0, len(linha) - 1):
        for y in range(0, len(linha) - 1):
            for z in range(0, len(linha) - 1):
                if linha[x][0] + linha[y][0] + linha[z][0] == 15 and linha[x][1] + linha[y][1] + linha[z][1] == 15 and linha[x][2] + linha[y][2] + linha[z][2] == 15:
                    print('\n\n')
                    print(linha[x])
                    print(linha[y])
                    print(linha[z])


quadrado_magico(input('Precione a tecla Enter'))
