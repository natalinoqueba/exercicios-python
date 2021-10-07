from random import choice


def dado(n=''):
    global jog
    dado_1 = list(range(1, 7))
    dado_2 = list(range(1, 7))
    d1 = choice(dado_1)
    d2 = choice(dado_2)
    pt = resutado(d1, d2, jog)
    jog += 1
    return pt


def resutado(d1, d2, jogada):
    global ponto, fim, pa
    soma = d1 + d2
    if jogada == 0 and (soma == 7 or soma == 11):
        print(f'\nObteve os dados: {d1} e {d2}'
              f'\nSoma dos dados: {soma}'
              f'\nResutado: Natural -- Voce ganhou')
        fim = True
    elif jogada == 0 and soma == 2 or soma == 12 or soma == 3:
        print(f'\nObteve os dados: {d1} e {d2}'
              f'\nSoma dos dados: {soma}'
              f'\nResutado: Craps --- Voce perdeu')
        fim = True
    else:
        ponto = soma
        if soma == 7:
            print(f'\nObteve os dados: {d1} e {d2}'
                  f'\nSoma dos dados: {soma}'
                  f'\nPonto: {pa}'
                  f'\nResutado:  Voce perdeu.')
            fim = True

        elif ponto == pa:
            print(f'\nObteve os dados: {d1} e {d2}'
                  f'\nSoma dos dados: {soma}'
                  f'\nPonto: {pa}'
                  f'\nResutado:  Voce Ganhou')
            fim = True
        else:
            if jogada == 0:
                pa = soma
            print(f'\nObteve os dados: {d1} e {d2}'
                  f'\nSoma dos dados: {soma}'
                  f'\nPonto: {pa}'
                  f'\nContinuar jogando...')
    return fim


jog = pa = ponto = 0
fim = True

while True:
    res = dado(input('Tecla enter para "lancar" os dados'))
    if res:
        break
