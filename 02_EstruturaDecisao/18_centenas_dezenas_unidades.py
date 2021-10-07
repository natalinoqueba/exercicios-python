print('Centenas, dezenas e unidades')
n = str(input('Digite um numero menor que 1000 : '))
nr = int(n)
if nr < 10:
    if n == '1':
        print(f'{n} unidade')
    else:
        print(f'{n} unidades')
elif nr < 100:
    if n[0] == '1':
        if n[1] == '1':
            print(f'{nr} = {n[0]} dezena e {n[1]} unidade')
        else:
            print(f'{nr} = {n[0]} dezena e {n[1]} unidades')
    else:
        if n[1] == '1':
            print(f'{nr} = {n[0]} dezenas e {n[1]} unidade')
        else:
            print(f'{nr} = {n[0]} dezenas e {n[1]} unidades')
elif nr < 1000:
    if n[0] == '1':
        if n[1] == '1':
            if n[2] == '1':
                print(f'{nr} = {n[0]} centena, {n[1]} dezena e {n[2]} unidade')
            else:
                print(f'{nr} = {n[0]} centena, {n[1]} dezena e {n[2]} unidades')
        else:
            if n[2] == '1':
                print(f'{nr} = {n[0]} centena, {n[1]} dezenas e {n[2]} unidade')
            else:
                print(f'{nr} = {n[0]} centena, {n[1]} dezenas e {n[2]} unidades')
    else:
        if n[1] == '1':
            if n[2] == '1':
                print(f'{nr} = {n[0]} centenas, {n[1]} dezena e {n[2]} unidade')
            else:
                print(f'{nr} = {n[0]} centenas, {n[1]} dezena e {n[2]} unidades')
        else:
            if n[2] == '1':
                print(f'{nr} = {n[0]} centenas, {n[1]} dezenas e {n[2]} unidade')
            else:
                print(f'{nr} = {n[0]} centenas, {n[1]} dezenas e {n[2]} unidades')
else:
    print('Entrada invalida!')
print('\n')
