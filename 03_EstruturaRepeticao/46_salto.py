while True:
    melhor = soma = 0
    pior = 50
    nome = input('Nome do atleta: ')
    if len(nome) == 0:
        break
    dist1 = float(input('Primeiro salto: '))
    if dist1 > melhor:
        melhor = dist1
    if dist1 < pior:
        pior = dist1
    soma += dist1
    dist2 = float(input('Segundo salto: '))
    if dist2 > melhor:
        melhor = dist2
    if dist2 < pior:
        pior = dist2
    soma += dist2
    dist3 = float(input('Terceiro salto: '))
    if dist3 > melhor:
        melhor = dist3
    if dist3 < pior:
        pior = dist1
    soma += dist3
    dist4 = float(input('Quarto salto: '))
    if dist4 > melhor:
        melhor = dist4
    if dist4 < pior:
        pior = dist4
    soma += dist4
    dist5 = float(input('Quinto salto: '))
    if dist5 > melhor:
        melhor = dist5
    if dist5 < pior:
        pior = dist5
    soma += dist5
    media = (soma - (melhor + pior))/3
    print(f'Atleta: {nome}')
    print(f'Primerio salto: {dist1}m\n'
          f'Segundo salto: {dist2}m\n'
          f'Terceiro salto: {dist3}m\n'
          f'Quarto salto: {dist4}m\n'
          f'Quinto salto: {dist5}m\n')
    print(f'Melhor salto: {melhor}m')
    print(f'Pior salto: {pior}m')
    print(f'Media dos demais saltos: {media:.1f}m\n')
    print(f'Resultado final:\n{nome}: {media:.1f}m')