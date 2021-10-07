notas = list()
soma = 0
nt = ''
for x in range(0, 4):
    notas.append(float(input('Introduza a nota: ')))
for x in range(0, 4):
    nt += f'{notas[x]}    '
    soma += notas[x]
print(f'Notas: {nt}  \nMedia: {soma/4}')