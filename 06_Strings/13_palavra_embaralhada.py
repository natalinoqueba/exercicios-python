from random import randrange, shuffle


def embaralha(palavra):
    p = ''
    plv = palavra.upper()
    pl = list()
    for x in plv:
        pl.append(x)
    shuffle(pl)
    for y in pl:
        p += f'{y}'
    return p


arq = open('11_palavras.txt', 'r')
arq.seek(randrange(0, 21))
arq.readline()
pal = arq.readline()
arq.close()
pal = pal.replace('\n', '')

erro = 0
print(f'{embaralha(pal)}')
while erro < 6:
    tentativa = input('Que palavra e? \nR:')
    if pal.upper() == tentativa.upper():
        print(f'A palavra e: {pal.upper()}\nVoce Voce ganhou!')
        break
    else:
        erro += 1
if erro == 6:
    print(f'A palavra e: {pal.upper()}\nVoce perdeu')
