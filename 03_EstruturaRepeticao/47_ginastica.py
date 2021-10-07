while True:
    melhor = soma = 0
    pior = 15
    nome = input('Nome do atleta: ')
    if len(nome) == 0:
        break
    for n in range(0, 7):
        nota = float(input('Nota: '))
        if nota > melhor:
            melhor = nota
        if nota < pior:
            pior = nota
        soma += nota
    media = (soma - (melhor + pior)) / 5
    print('Resultado final: ')
    print(f'Atleta: {nome}\n'
          f'Melhor nota: {melhor}\n'
          f'Pior nota: {pior}\n'
          f'Media: {media}')
