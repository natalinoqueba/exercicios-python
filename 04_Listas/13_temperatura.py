meses = ('Janeiro', 'Fevereiro', 'Marco', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
temperaturas = list()
media = 0.0
for mes in meses:
    temperaturas.append(float(input(f'Media da temperatura de {mes}: ')))
for x in temperaturas:
    media += x
media = media/12
print(f'\n\nMedia das temperaturas: {media:.2f}\nMeses com a temperatura maior que a media anual:')
for y, mes in enumerate(meses):
    if temperaturas[y] > media:
        print(f'{mes} - {int(temperaturas[y])}')