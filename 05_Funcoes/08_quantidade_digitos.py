def quantidade_digitos(nr):
    num = str(nr)
    if num[0] == '-':
        print(f'O numero {nr} tem {len(num) - 1} digitos.')
    else:
        print(f'O numero {nr} tem {len(num)} digitos.')



quantidade_digitos(int(input('Digite um numero inteiro qualquer: ')))
