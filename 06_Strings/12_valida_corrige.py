ls = list()
c = 0
tel_1 = tel_2 = ''

print('Valida e corrige numero de telefone')
telefone = input('Telefone: ')
if '-' in telefone:
    telefone = telefone.replace('-', '')
    if len(telefone) == 7:
        print('Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.')
        for x in range(0, len(telefone)):
            ls.append(telefone[x])
        ls.insert(0, '3')
        for y in ls:
            tel_1 += y
            c += 1
            tel_2 += y
            if c == 4:
                tel_2 += '-'
    else:
        tel_1 = telefone
        for x in range(0, len(telefone)):
            ls.append(telefone[x])
        ls.insert(0, '3')
        for y in ls:
            tel_2 += y
            if c == 4:
                tel_2 += '-'

else:
    if len(telefone) == 7:
        print('Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.')
        for x in range(0, len(telefone)):
            ls.append(telefone[x])
        ls.insert(0, '3')
        for y in ls:
            tel_1 += y
            c += 1
            tel_2 += y
            if c == 4:
                tel_2 += '-'
    else:
        tel_1 = telefone
        for x in range(0, len(telefone)):
            ls.append(telefone[x])
        for y in ls:
            c += 1
            tel_2 += y
            if c == 4:
                tel_2 += '-'

print(f'Telefone corrigido sem formatação: {tel_1}'
      f'\nTelefone corrigido com formatação: {tel_2}')
