n = int(input('Montar tabuada de : '))
i = int(input('Comecar por : '))
f = int(input('Terminar em : '))
while f < i:
    print('Numero invalido')
    f = int(input('Terminar em : '))
print(f'\nTabuada de 5 comecando em {i} e terminando em {f}:')
for x in range(i, f + 1):
    print(f'{n} x {x} = {n * x}')
