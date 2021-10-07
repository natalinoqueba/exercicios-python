while True:
    res = 1
    n = int(input('Entre com um numero(positivo menor que 16): '))
    if n > 15:
        print('Numero nao valido!!!')
    else:
        for x in range(n, 1, -1):
            res *= x
        print(f'{n}! = {res}')
    p = input('Deseja parar?(s/n)')
    if p == 's':
        break