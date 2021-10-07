from random import choice
aleatorio = list()
al = list(range(0, 100))
stp = 0
for y in range(0, 100):
    z = choice(al)
    aleatorio.append(z)
for x in aleatorio:
    print(f'{x} foi repetido {aleatorio.count(x)}')
