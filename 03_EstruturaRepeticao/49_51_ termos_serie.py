n = int(input('Numero de termos: '))
s = 0
m = 1
print('S = ', end='')
for nr in range(1, n):
    s += nr / m
    print(f' {nr}/{m} +', end='')
    m += 2
print(f' {nr+1}/{m}', end='')
s += nr / m
print(f' = {s:.2f}')