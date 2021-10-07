numero = int(input('Deseja ver a tabuada de que numero? (1 - 10): '))
for x in range(1, 11):
    res = numero * x
    print(f'{numero} x {x} = {res}')
