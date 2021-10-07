res= 1
fat = ''
n = int(input('Entre com um numero: '))
for x in range(n, 0, -1):
    if x == n:
        fat += f'{x} '
    elif x == 1:
        fat += f'. {x}'
    else:
        fat += f'. {x} '
    res *= x
print(f'Fatorial de: {n}')
print(f'{n}! = {fat} = {res}')