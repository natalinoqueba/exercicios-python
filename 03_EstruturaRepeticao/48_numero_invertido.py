nr = int(input('Digite um numero inteiro: '))
nr2 = str(nr)
nr3 = ''
for x in range(len(nr2) - 1, -1, -1):
    nr3 += nr2[x]
print(f'{nr}\n=> {nr3}')