nota = nota1 = notas = 0
while True:
    nota = float(input('Digite a nota: '))
    nota1 += nota
    notas += 1
    p = input('Deseja para de introduzir as notas? (s/n): ')
    if p == 's':
        break
print(f'Media das notas: {nota1/notas}')
