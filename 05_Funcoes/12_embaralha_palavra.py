from random import shuffle


def embaralha(palavra):
    p = ''
    plv = palavra.lower()
    pl = list()
    for x in plv:
        pl.append(x)
    shuffle(pl)
    for y in pl:
        p += f'{y}'
    return p


pal = embaralha(input('Digite qualquer palavra: '))
print(pal)
