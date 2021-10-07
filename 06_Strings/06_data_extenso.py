mes = ('Janeiro', 'Fevereiro', 'Marco', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
print('Formato da data: dd/mm/aaaa')
data = input('Data de nascimento: ')
m = int(data[3:5]) - 1
print(f'Voce nasceu em {data[:2]} de {mes[m]} de {data[6:]}')
