i = ''
p = d = 0
n1 = int(input('Digite um numero para saber quantos numeros primos existem de 1 ate esse mesmo numero: '))
for n2 in range(1, n1+1):
    p = 0
    for x in range(1, n2+1):
        if n2 % x == 0:
            p += 1
        d += 1
    if p == 2:
        i += str(f' {n2}')
print(f'Numeros primos de 1 a {n1}: 1 {i}\nNumero de divisoes feitas: {d}')
