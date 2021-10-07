import random

aleatorio = list()
stp = 0
al = [x for x in range(0, 1000)]
random.shuffle(al)
for y in al:
    stp += 1
    if stp == 100:
        break
    aleatorio.append(y)
print(aleatorio)
for x in aleatorio:
    print(f'{x} foi repetido {aleatorio.count(x)}')
