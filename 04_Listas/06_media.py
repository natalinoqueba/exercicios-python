media = list()
nota = md = 0
for x in range(0, 10):
    md = nota = 0
    print(f'Aluno {x + 1}:')
    for y in range(0, 4):
        nota += int(input(f'Introduza a {y + 1} nota: '))
    md = nota / 4
    media.append(md)
print(media)
