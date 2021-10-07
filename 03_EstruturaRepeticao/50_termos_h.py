n = int(input('Numero de termos: '))
h = 0
m = 1
print('H = ', end='')
for nr in range(1, n):
    h += m / nr
    print(f' {m}/{nr} +', end='')
nr += 1
h += m / nr
print(f' {m}/{nr}', end='')
print(f' = {h:.2f}')