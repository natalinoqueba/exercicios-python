st_1 = input('String 1: ')
st_2 = input('String 2: ')

tamanho_1 = len(st_1)
tamanho_2 = len(st_2)
print(f'Tamanho de "{st_1}": {tamanho_1}')
print(f'Tamanho de "{st_2}": {tamanho_2}')
if tamanho_1 == tamanho_2:
    print('As strigns tem mesmo tamanho')
    if st_1 == st_2:
        print('As duas strings possuem conteudo igual.')
else:
    print('As duas strings sao de tamanhos diferentes.')
    print('As duas strings possuem conteudo diferente.')
