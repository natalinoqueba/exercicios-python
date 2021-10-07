def data(dia, mes, ano):
    m = ('Janeiro', 'Fevereiro', 'Marco', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
    if dia > 31 or dia < 1 or mes > 12 or mes < 1:
        return 'NULL'
    else:
        dt = f'{dia} de {m[mes - 1]} de {ano}'
    return dt


print('Formato: dd/mm/aaaa')
di = int(input('Dia: '))
m = int(input('Mes: '))
a = int(input('Ano: '))
d = data(di, m, a)
print(f'{di}/{m}/{a} => {d}')
