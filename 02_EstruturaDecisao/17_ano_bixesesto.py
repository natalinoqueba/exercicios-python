ano = int(input('Numero correspondente a um ano: '))
if ano > 0:
    if ano % 4 == 0:
        if ano % 100 != 0:
            print('2')
            print(f'O ano {ano} e bissexto!')
    elif 2000 % 400 == 0:
        print(f'O ano {ano} nao e bissexto!')
    elif ano % 400 != 0:
        print(f'O ano {ano} nao e bissexto!')
else:
    print('Ano invalido')
