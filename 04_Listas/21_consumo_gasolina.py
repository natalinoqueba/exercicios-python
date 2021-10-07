carros = list()
km_litro = list()
menor = 0
menor_preco = ''
print('Comparativo de Consumo de Combustível')
for x in range(0, 5):
    print(f'Veiculo {x+1}')
    carros.append(input('Nome: '))
    km_litro.append(float(input('Km por litro: ')))
print('\nRelatório Final')
for y in range(0, 5):
    consumo_mil = 1000/km_litro[y]
    preco_mil = (1000/km_litro[y]) * 2.25
    if menor == 0:
        menor_preco = carros[y]
    elif preco_mil < menor:
        menor_preco = carros[y]
    print(f'{y+1} - {carros[y]:6} - {km_litro[y]:4} - {consumo_mil:.1f} - {preco_mil:.2f}')
print(f'O menor consumo é do {menor_preco}.')
