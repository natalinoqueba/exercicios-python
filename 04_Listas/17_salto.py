nomes = list()
saltos = list()
salto = list()
soma = media = 0
while True:
    nome = input('Nome do atelta(fim - para encerrar o programa): ')
    if nome == 'fim':
        break
    else:
        salto.clear()
    nomes.append(nome)
    for x in range(0, 5):
        salto.append(float(input(f'{x + 1}o salto: ')))
    saltos.append(salto[:])
print(f'\n\nResultado final:')
for y, nome in enumerate(nomes):
    print(f'\nAtleta: {nome}')
    print(f'Saltos: ', end='')
    for slt in saltos[y]:
        print(slt, end='    ')
        soma += slt
    print()
    media = soma / 5
    print(f'Media dos saltos: {media:.2f} m')
    soma = media = 0