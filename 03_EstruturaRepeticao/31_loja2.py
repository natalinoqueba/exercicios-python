p = prod = soma = dinh = troco = 0
while True:
    print('')
    print('=' * 20)
    print('Loja Tabajara')
    p = prod = soma = dinh = troco = 0
    while True:
        p += 1
        prod = float(input(f'Produto {p}: Mzn '))
        soma += prod
        if prod == 0:
            break
    print(f'Total: Mzn {soma}')
    dinh = float(input('Dinheiro: Mzn '))
    troco = dinh - soma
    print(f'Troco: Mzn {troco}')
    print('=' * 20)
