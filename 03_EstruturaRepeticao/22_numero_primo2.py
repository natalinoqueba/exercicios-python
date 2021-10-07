d = ''
p = 0
n = int(input('Digite um numero: '))
for x in range(1, n+1):
    if n % x == 0:
        p += 1
        d += str(f' {x}')
if p == 2:
    print(f'{n} e um numero primo!')
else:
    print(f'{n} nao e primo! e divisivel pelos numeros{d}.')