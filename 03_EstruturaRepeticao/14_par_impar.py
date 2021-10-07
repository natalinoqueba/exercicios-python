i = p = 0
for n in range(1, 11):
    nu = int(input('Digite um numero inteiro: '))
    if nu % 2 == 0:
        p += 1
    else:
        i += 1
print(f'Ha {p} numeros pares e {i} impares!')