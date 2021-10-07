def converter(esp):
    esp = esp / 1048576
    return esp


def percentual(e, total):
    perc = e * 100 / total
    return perc


nome = list()
espaco = list()
nr = medio = soma = 0

arq = open('usuarios.txt', 'r')
for n in arq:
    nome.append(n[:16])
    espaco.append(int(n[16:]))
arq.close()

for v in espaco:
    soma += converter(int(v))

relatorio = open('relatorio.txt', 'w')  # cria arquivo relatorio
relatorio.write('ACME Inc.          Uso do espaço em disco pelos usuários\n')
relatorio.write('-' * 60)
relatorio.write('\nNr.     Usuário        Espaço utilizado        % do uso')
for x in range(0, len(nome)):
    nr += 1
    relatorio.write(f'\n{nr}      {nome[x].capitalize()}       {converter(espaco[x]):8.2f} MB     {percentual(converter(espaco[x]), soma):5.2f}%')
relatorio.write(f'\n\nEspaço total ocupado: {soma:.2f} MB')
relatorio.write(f'\nEspaço médio ocupado: {(soma / nr):.2f} MB')
relatorio.close()

r = open('relatorio.txt', 'r')
print(r.read())
