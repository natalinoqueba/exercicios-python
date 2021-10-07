altmaior = altmenor = nrmenor = nrmaior = 0
for aluno in range(1, 11):
    numaluno = int(input('Numero do aluno: '))
    altaluno = float(input('Altura do aluno: '))
    if altaluno > altmaior:
        altmaior = altaluno
        nrmaior = numaluno
    elif altmenor > altaluno:
        altmenor = altaluno
        nrmenor = numaluno
    if altmenor == 0:
        altmenor = altaluno
        nrmenor = numaluno
print(f'Aluno nr: {nrmaior}     Mais alto: {altmaior}m')
print(f'Aluno nr: {nrmenor}     Mais baixo: {altmenor}')
