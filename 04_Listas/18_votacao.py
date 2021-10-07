def percentual(total_volto, voto_jogador):
    perc = voto_jogador * 100 / total_volto
    return perc


jogadores = list()  # Vai armazenar so o numero dos jogadores votados
melhor = nv = vot_jog = percentual_melhor = 0
print('Enquente: Quem foi o melhor jogador?')
while True:
    jogador = int(input('Numero do jogador(0 = fim): '))
    if jogador == 0:
        break
    if jogador > 23 or jogador < 1:
        print('Informe um valor entre 1 e 23 ou 0 para sair!')
        jogador = int(input('Numero do jogador(0 = fim): '))
        if jogador == 0:
            break
    jogadores.append(jogador)
nr_votos = len(jogadores)
print(f'\nResultado da votacao:\n\nForam computados: {nr_votos}')
print('\nJogador      Votos       Percentual')
jogadores.sort()
jog_set = set(jogadores)  # converte a lista para set
for j in jog_set:
    nr_v = jogadores.count(j)
    percentual_melhor = percentual(nr_votos, nr_v)
    if nr_v > melhor:
        melhor = j
        nv = nr_v
        percentual_melhor = percentual_melhor
    print(f'{j:2}     {nr_v:10}        {percentual_melhor:6.1f}%')
print(f'O melhor jogador foi o numero {melhor}, com {nv} votos, correspondendo a {percentual_melhor}% do total de votos.')
