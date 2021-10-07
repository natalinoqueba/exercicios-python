nr = list()
soma = 0
mult = 1
for x in range(0, 5):
    nr.append(int(input('Digite um numero inteiro: ')))
for n in nr:
    soma += n
    mult *= n
print(f'{nr}\n{soma}\n{mult}')
