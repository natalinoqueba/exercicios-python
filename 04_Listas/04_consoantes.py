carat = list()
s = 0
c = ''
for x in range(0, 10):
    carat.append(input('Introduza um caracter:'))
for x in carat:
    if x not in 'aeiou':
        s += 1
        c += x
print(f'Numero de consoantes: {s}\n{c}')