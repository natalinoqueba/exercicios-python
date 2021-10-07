from random import randrange

arq = open('11_palavras.txt', 'r')
arq.seek(randrange(1, 21))
arq.readline()
palavra = arq.readline().upper()
palavra.replace('\n', '')
pal = list()
for x in range(0, len(palavra) - 1):
    pal.append(' _ ')

erro = 0
while erro < 6:
    letra = input('Digite uma letra: ')
    while len(letra) > 1:
        print('Digite somente uma letra!!')
        letra = input('Digite uma letra: ')
    if letra.upper() not in palavra:
        erro += 1
        print(f'Voce errou pela {erro}a vez! Tente novamente')
    else:
        print('A palavra e: ',  end='')
        for x in range(0, len(palavra)):
            if letra.upper() == palavra[x]:
                pal[x] = letra.upper()
        for x in pal:
            print(x, end='')
        print()
        if ' _ ' not in pal:
            break
if erro < 6:
    print('Voce ganhou!')
else:
    print('Voce perdeu!')