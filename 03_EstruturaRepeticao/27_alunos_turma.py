alunos = totalalunos = media = 0
quantidade_turma = int(input('Quantidade de turmas: '))
for x in range(1, quantidade_turma + 1):
    while alunos <= 0 or alunos > 40:
        alunos = int(input(f'Numero de alunos da {x}a turma: '))
        if alunos <= 0 or alunos > 40:
            print("A turma deve ter ate 40 alunos")
    totalalunos += alunos
    alunos = 0
media = float(totalalunos / quantidade_turma)
print(f'Media de alunos por turma: {media}')
