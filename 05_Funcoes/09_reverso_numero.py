def reverso_numero(nr):
    num = str(nr)
    print(f'{nr} => ', end='')
    if num[0] == '-':
        print('-', end='')
        for n in range(len(num) - 1, 0, -1):
            print(num[n], end='')
    else:
        for n in range(len(num) - 1, -1, -1):
            print(num[n], end='')


reverso_numero(int(input('Digite um numero qualquer: ')))
