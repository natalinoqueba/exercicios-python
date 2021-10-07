from time import sleep


def linha(msg):
    print('===================')
    print(msg)
    print('===================')


linha('Jogo da forca')
palavra_secreta = 'banana'
letras_acertadas = ['_', '_', '_', '_', '_', '_']
acertou = False
enforcou = False
erros = 0

print(letras_acertadas)
while not acertou and not enforcou:
    chute = input('Qual letra?')
    posicao = 0
    for letra in palavra_secreta:
        if chute.upper() == letra.upper():
            letras_acertadas[posicao] = letra
        posicao = posicao + 1
    else:
        erros += 1
    enforcou = erros == 6
    acertou = '_' not in letras_acertadas
    print(letras_acertadas)

if acertou:
    print('Voce ganhou!!!')
else:
    print('Voce perdeu!!')
linha('Fim')
sleep(10)

