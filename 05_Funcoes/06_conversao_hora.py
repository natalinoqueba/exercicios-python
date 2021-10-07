def converter(hora, minuto):
    if hora > 12:
        hr = hora - 12
        mn = minuto
        ap = 'P'
    else:
        hr = hora
        mn = minuto
        ap = 'A'
    saida_convertida(hr, mn, ap)


def saida_convertida(h, m, ap):
    if ap == 'A':
        print(f'{h}:{m} A.M')
    else:
        print(f'{h}:{m} P.M')


while True:
    ho = int(input('Hora: '))
    mi = int(input('Minuto: '))
    while ho > 24 or ho < 0 or mi > 60 or mi < 0:
        print('Dados introduzidos invalidos!')
        ho = int(input('Hora: '))
        mi = int(input('Minuto: '))
    converter(ho, mi)
    cont = input('Deseja continuar(S/N): ')
    if cont.upper() == 'N':
        break
