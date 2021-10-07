so = ('Windows Server', 'Unix        ', 'Linux        ', 'Netware     ', 'Mac OS      ', 'Outro       ')
votos = list()
mais_votado = maior_nr = maior_percent = total = 0
print('As possíveis respostas são:\n1- Windows Server\n2- Unix\n3- Linux\n4- Netware\n5- Mac OS\n6- Outro\n0- Fim')
while True:
    voto = int(input('Qual o melhor Sistema Operacional para uso em servidores?: '))
    if voto == 0:
        break
    elif voto < 1 or voto > 6:
        print('Opcao invalida!')
        voto = int(input('Qual o melhor Sistema Operacional para uso em servidores?: '))
        if voto == 0:
            break
    votos.append(voto)
print(f'Sistema Operacional      Votos       %')
for x, sistema in enumerate(so):
    percent = (votos.count(x+1) / len(votos)) * 100
    print(f'{sistema}{votos.count(x+1):7}      {percent:.2f}')
    if percent > maior_percent:
        maior_percent = percent
        mais_votado = sistema
        maior_nr = votos.count(x+1)
total = len(votos)
print(f'Total         {total}'
      f'\nO Sistema Operacional mais votado foi o {mais_votado}, com {maior_nr} votos, correspondendo a {maior_percent:.2f}% dos votos.')
