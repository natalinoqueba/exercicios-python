n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
if n1 > n2:
    for x in range(n1 - 1, n2, -1):
        print(x)
else:
    for x in range(n1 + 1, n2):
        print(x)

