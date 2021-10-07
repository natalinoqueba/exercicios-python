def numero(n):
    for x in range(1, n+1):
        for y in range(1, x+1):
            print(f'{y:3}', end=' ')
        print()


numero(int(input('Digite um numero inteiro: ')))
