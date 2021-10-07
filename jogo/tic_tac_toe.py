def imprimir_quadrado(posicao, jogador):
    global empate
    if quadrado[posicao] != '':
        print('Posicao ja foi preenchida!')
        imprimir_quadrado(int(input(f'Posicao a jogar({jog}): ')) - 1, jogada)
    quadrado[posicao] = jogador

    print(f'+----+----+----+')
    print(f'|  {quadrado[0]:2}|  {quadrado[1]:2}|  {quadrado[2]:2}|')
    print(f'|----+----+----|')
    print(f'|  {quadrado[3]:2}|  {quadrado[4]:2}|  {quadrado[5]:2}|')
    print(f'|----+----+----|')
    print(f'|  {quadrado[6]:2}|  {quadrado[7]:2}|  {quadrado[8]:2}|')
    print(f'+----+----+----+')
    empate = verificar()


def verificar():
    vertical_j1 = quadrado[0] == quadrado[1] == quadrado[2] == j['jogador 1'] != '' or quadrado[3] == quadrado[4] == \
                  quadrado[5] == j['jogador 1'] != '' or quadrado[6] == quadrado[7] == quadrado[8] == j['jogador 1'] != \
                  ''
    horizontal_j1 = quadrado[0] == quadrado[3] == quadrado[6] == j['jogador 1'] != '' or quadrado[1] == quadrado[4] == \
                    quadrado[7] == j['jogador 1'] != '' or quadrado[2] == quadrado[5] == quadrado[8] == j[
                        'jogador 1'] != ''
    obli_j1 = quadrado[0] == quadrado[4] == quadrado[8] == j['jogador 1'] != '' or quadrado[2] == quadrado[4] == \
              quadrado[6] == j['jogador 1'] == j['jogador 1'] != ''
    vertical_j2 = quadrado[0] == quadrado[1] == quadrado[2] == j['jogador 2'] != '' or quadrado[3] == quadrado[4] == \
                  quadrado[5] == j['jogador 2'] != '' or quadrado[6] == quadrado[7] == quadrado[8] == j[
                      'jogador 2'] != ''
    horizontal_j2 = quadrado[0] == quadrado[3] == quadrado[6] == j['jogador 2'] != '' or quadrado[1] == quadrado[4] == \
                    quadrado[7] == j['jogador 2'] != '' or quadrado[2] == quadrado[5] == quadrado[8] == j[
                        'jogador 2'] != ''
    obli_j2 = quadrado[0] == quadrado[4] == quadrado[8] == j['jogador 2'] != '' or quadrado[2] == quadrado[4] == \
              quadrado[6] == j[
                  'jogador 2'] != ''
    if vertical_j1 or horizontal_j1 or obli_j1:
        print('Jogador 1 venceu!')
        return False
    elif vertical_j2 or horizontal_j2 or obli_j2:
        print('Jogador 2 venceu!')
        return False
    else:
        return True


def entrada_dado(dado):
    if dado.upper() == 'X':
        j['jogador 1'] = dado.upper()
        j['jogador 2'] = 'O'
        print('Jogador 1 vai usar X e jogador 2 vai usar O')
    elif dado.upper() == 'O':
        j['jogador 1'] = dado.upper()
        j['jogador 2'] = 'X'
        print('Jogador 1 vai usar O e jogador 2 vai usar X')


j = {'jogador 1': '', 'jogador 2': ''}
quadrado = [''] * 9
empate = True
q = [1, 2, 3, 4, 5, 6, 7, 8, 9]
entrada_dado(input('Escolha o tipo de dado jogador 1 (X/O): '))
print(f'+----+----+----+'
      f'\n|  {q[0]:2}|  {q[1]:2}|  {q[2]:2}|'
      f'\n|----+----+----|'
      f'\n|  {q[3]:2}|  {q[4]:2}|  {q[4]:2}|'
      f'\n|----+----+----|'
      f'\n|  {q[6]:2}|  {q[7]:2}|  {q[8]:2}|'
      f'\n+----+----+----+')
while '' in quadrado:
    for jog, jogada in j.items():
        imprimir_quadrado(int(input(f'Posicao a jogar({jog}): ')) - 1, jogada)
        if not empate or '' not in quadrado:
            break
    if not empate or '' not in quadrado:
        break
if empate:
    print('EMPATE')
print('Queba')