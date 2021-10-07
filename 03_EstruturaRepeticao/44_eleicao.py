print('=' *20)
print('Codigos de votacao:\n'
      '1 - Jose Silva\n'
      '2 - Joao Danie\n'
      '3 - Felisberta Damiao\n'
      '4 - Lucio Mateus\n'
      '5 - Voto nulo\n'
      '6 - Voto em branco\n\n')
print('=' *20)
voto = 7
voto1 = voto2 = voto3 = voto4 = nulo = total = branco = 0
while voto != 0:
    voto = int(input('Codigo de votacao: '))
    if voto > 6 or voto < 0:
        print('Codigo invaldo!')
        voto = int(input('Codigo de votacao: '))
    if voto == 1:
        voto1 += 1
    elif voto == 2:
        voto2 += 1
    elif voto == 3:
        voto3 += 1
    elif voto == 4:
        voto4 += 1
    elif voto == 5:
        nulo += 1
    elif voto == 6:
        branco += 1
    total += 1
vtnulo = (nulo * 100) / total
vtbranco = (branco * 100) / total
print('\n\n')
print('Candidato        Nr de votos')
print(f'Jose Silva     {voto1} '
      f'Joao Danie      {voto2}' 
      f'Felisberta Damiao       {voto3}'
      f'Lucio Mateus        {voto4}')
print(f''
      f'Votos nulos: {nulo}'
      f'Votos em branco: {branco}'
      f'Percentagem dos votos nulos: {vtnulo}'
      f'Percentagem dos votos em branco: {vtbranco}')