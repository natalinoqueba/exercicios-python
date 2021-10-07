res= 1
n = int(input('Entre com um numero: '))
for x in range(n, 1, -1):
    res *= x
print(f'{n}! = {res}')