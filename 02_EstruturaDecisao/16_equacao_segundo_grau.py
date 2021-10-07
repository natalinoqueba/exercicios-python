from time import sleep
from math import sqrt

print('»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»')
print('Calculo de equaçao de segundo grau')
print('"ax2+bx+c"')
print('««««««««««««««««««««««««««««««««««\n')
delta = 0
raiz1 = 0
raiz2 = 0

a = float(input('Valor de "a": '))
if a == 0:
    print('A equaçao nao e de segundo grau! A encerrar o programa...')
    sleep(5)
else:
    b = float(input('Valor de "b": '))
    c = float(input('Valor de "c": '))
    print('\n')
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print('A equaçao nao possui raizes reais! A encerrar o programa...')
        sleep(5)
    elif delta == 0:
        raiz1 = -b / 2 * a
        print(f'\nA equaçao possue apenas uma raiz real!')
        if b < 0 < c:
            print(f'{a}x2{b}x+{c}')
        elif b < 0 and c < 0:
            print(f'{a}x2{b}x{c}')
        elif b > 0 > c:
            print(f'{a}x2+{b}x{c}')
        else:
            print(f'{a}x2+{b}x+{c}')
        print(f'Delta = {delta}')
        print(f'Raiz = {raiz1}')
    elif delta > 0:
        raiz1 = (-b + sqrt(delta)) / 2 * a
        raiz2 = (-b - sqrt(delta)) / 2 * a
        if b < 0 < c:
            print(f'{a}x2{b}x+{c}')
        elif b < 0 and c < 0:
            print(f'{a}x2{b}x{c}')
        elif b > 0 > c:
            print(f'{a}x2+{b}x{c}')
        else:
            print(f'{a}x2+{b}x+{c}')
        print(f'\nDelta = {delta}')
        print(f'Raiz 1 = {raiz1}')
        print(f'Raiz 2 = {raiz2}')

