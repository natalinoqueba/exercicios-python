c1 = c2 = c3 = 0
print('Candidato 1: Filipe (codigo c1)\nCandidato 2: Antonio (codigo c2)\nCandidato 3: Jose (codigo c3)')
nre = int(input('Numero de eleitores: '))
for x in range(0, nre):
    v = input('Codigo do candidato: ')
    if v == 'c1':
        c1 += 1
    elif v == 'c2':
        c2 += 1
    elif v == 'c3':
        c3 += 1
print('Candidato    Nr de votos')
print(f'Filipe  {c1:7}\nAntonio   {c2:5}\nJose  {c3:9}')