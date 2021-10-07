defeito_mouse = list()
defeito = ('1- necessita da esfera ', '2- necessita de limpeza', '3- necessita troca do cabo ou conector', '4- quebrado ou inutilizado')
print('Opcoes validas:'
      '\n1- necessita da esfera;'
      '\n2- necessita de limpeza;'
      '\n3- necessita troca do cabo ou conector;'
      '\n4- quebrado ou inutilizado.')
while True:
    defeit = int(input('Situacao do mouse: '))
    if defeit == 0:
        break
    elif defeit > 4:
        print('Opcao Invalida')
        defeit = int(input('Situacao do mouse: '))
    defeito_mouse.append(defeit)
print(f'\n\nQuantidade de mouses: {len(defeito_mouse)}'
      f'\nSituação                            Quantidade  Percentual')
for x, dft in enumerate(defeito):
    percentual = (defeito_mouse.count(x+1) * 100)/len(defeito_mouse)
    print(f'{dft:40}    {defeito_mouse.count(x+1)}     {percentual:.2f}')
