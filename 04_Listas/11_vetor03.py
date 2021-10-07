a = list()
b = list()
c = list()
d = list()
for x in range(0,  10):
    a.append(int(input('Digite um numero inteiro(lista A):')))
for x in range(0,  10):
    b.append(int(input('Digite um numero inteiro(lista B):')))
for x in range(0,  10):
    c.append(int(input('Digite um numero inteiro(lista D):')))
for x in range(0,  10):
    d.append(a[x])
    d.append(b[x])
    d.append(c[x])
print(f'Lista A: {a}\nLista B: {b}\nLista C: {c}\nLista D: {d}')
