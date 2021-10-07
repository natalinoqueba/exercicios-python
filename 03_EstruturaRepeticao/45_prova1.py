maiornota = totalalunos = nota = media = 0
menornota = 10
print('Exemplo do gabarito ABBDCBEADB')
gabarito = input('Gabarito da prova(em sequencia): ').upper()
while len(gabarito) != 10:
    gabarito = input('Gabarito da prova(em sequencia): ').upper()
while True:
    nota = 0
    for quest in range(1, 11):
        resp = input(f'Resposta da {quest} questao: ')
        while resp not in 'ABCDE':
            print('Opcao invalida')
            resp = input(f'Resposta da {quest} questao: ')
        if quest == 1 and resp.upper() == gabarito[0]:
            nota += 1
        elif quest == 2 and resp.upper() == gabarito[1]:
            nota += 1
        elif quest == 3 and resp.upper() == gabarito[2]:
            nota += 1
        elif quest == 4 and resp.upper() == gabarito[3]:
            nota += 1
        elif quest == 5 and resp.upper() == gabarito[4]:
            nota += 1
        elif quest == 6 and resp.upper() == gabarito[5]:
            nota += 1
        elif quest == 7 and resp.upper() == gabarito[6]:
            nota += 1
        elif quest == 8 and resp.upper() == gabarito[7]:
            nota += 1
        elif quest == 9 and resp.upper() == gabarito[8]:
            nota += 1
        elif quest == 10 and resp.upper() == 'A':
            nota += 1
    if nota > maiornota:
        maiornota = nota
    if nota < menornota:
        menornota = nota
    totalalunos += 1
    media += nota
    cont = input('Outro aluno vai utilizar o sistema(S/N): ')
    if cont.upper() == 'N':
        while cont not in 'SN':
            cont = input('Outro aluno vai utilizar o sistema(S/N): ')
        break
print(f'Maior acerto: {maiornota}\n'
      f'Menor acerto: {menornota}\n'
      f'Total de alunos que utilizaram o sistema: {totalalunos}\n'
      f'Media das notas da turma: {media / totalalunos}')
