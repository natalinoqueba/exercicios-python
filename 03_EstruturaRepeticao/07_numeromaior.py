n1 = float(input('Entre com um numero: '))
n2 = float(input('Entre com um outro numero: '))
n3 = float(input('Entre com um outro numero: '))
n4 = float(input('Entre com um outro numero: '))
n5 = float(input('Entre com um outro numero: '))
if n2 < n1 > n3 and n5 < n1 > n4:
    print(f'O maior numero e {n1}')
elif n1 < n2 > n3 and n5 < n2 > n4:
    print(f'O maior numero e {n2}')
elif n1 < n3 > n2 and n5 < n3 > n4:
    print(f'O maior numero e {n3}')
elif n1 < n4 > n3 and n5 < n4 > n2:
    print(f'O maior numero e {n4}')
elif n1 < n5 > n3 and n2 < n5 > n4:
    print(f'O maior numero e {n5}')