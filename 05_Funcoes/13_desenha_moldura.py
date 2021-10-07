def desenhar(lag='', com=''):
    lg = int(lag)
    cm = int(com)
    if lg > 20:
        lg = int(lg / 2)
        print(f'Novo valor da largura: {lg}')
    elif lg < 1:
        lg = lg * (-3)
        print(f'Novo valor da largura: {lg}')
    if cm > 20:
        cm = int(lg / 2)
        print(f'Novo valor da largura: {cm}')
    elif cm < 1:
        cm = cm * (-3) + 1
        print(f'Novo valor da largura: {cm}')
    print('+', '-' * lg, '+')
    for x in range(0, cm):
        print('|', ' ' * lg, '|')
    print('+', '-' * lg, '+')


print('Desenha Moldura\nValor max aceitavel: 20\n Valor min aceitavel: 1')
desenhar(input('Valor da largura: '), input('Valor do comprimento: '))
