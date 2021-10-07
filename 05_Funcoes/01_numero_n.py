def numero(n):
    for x in range(1, n+1):
        print(f'{x:3} ' * x)


numero(int(input('Digite um numero inteiro: ')))
