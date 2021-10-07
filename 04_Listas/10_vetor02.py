c = list()
a = [x for x in range(0,  10)] # cria lista com numeros de 0 a 9
b = [x for x in range(0,  10)]
for x in range(0,  10):
    c.append(a[x])
    c.append(b[x])
print(f'Lista A: {a}\nLista B: {b}\nLista C: {c}')
