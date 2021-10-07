print('Entre com uma data(dd/mm/aaaa)')
dia = int(input('Dia: '))
mes = int(input('Mes: '))
ano = int(input('Ano: '))
if ano % 4 == 0:
    if ano % 100 != 0:
        if 0 < mes < 13:
            if mes != 2:
                if 0 < dia < 32:
                    print('Data valida!')
                    print(f'{dia}/{mes}/{ano}')
                else:
                    print('Data invalida!')
            else:
                if 0 < dia < 30:
                    print('Data valida')
                    print(f'{dia}/{mes}/{ano}')
                else:
                    print('Data invalida!')
        else:
            print('Data invalida!')
elif ano % 400 != 0:
    if 0 < mes < 13:
        if mes != 2:
            if 0 < dia < 32:
                print('Data valida!')
                print(f'{dia}/{mes}/{ano}')
            else:
                print('Data invalida!')
        else:
            if 0 < dia < 29:
                print('Data valida')
                print(f'{dia}/{mes}/{ano}')
            else:
                print('Data invalida!')
    else:
        print('Data invalida!')
elif ano % 400 == 0:
    if 0 < mes < 13:
        if mes != 2:
            if 0 < dia < 32:
                print('Data valida!')
                print(f'{dia}/{mes}/{ano}')
            else:
                print('Data invalida!')
        else:
            if 0 < dia < 30:
                print('Data valida')
                print(f'{dia}/{mes}/{ano}')
            else:
                print('Data invalida!')
    else:
        print('Data invalida!')
