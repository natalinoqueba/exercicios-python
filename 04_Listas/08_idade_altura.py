idade = list()
altura = list()
for x in range(0, 5):
    idade.append(int(input('Idade: ')))
    altura.append(float(input('Altura: ')))
for y in range(4, -1, -1):
    print(f'Idade: {idade[y]}  Altura:{altura[y]}')