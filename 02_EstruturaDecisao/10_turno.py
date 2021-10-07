# Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.


print('M - Matutino/V - Vesperino/N - Noturno\n\nResponda com a letra correspondente...')
turno = str(input('Em que turno voce estuda?\nR: '))
if turno == 'M' or turno == 'm':
    print('Bom Dia!')
elif turno == 'V' or turno == 'v':
    print('Boa Tarde!')
elif turno == 'N' or turno == 'n':
    print('Boa Noite!')
else:
    print('Valor Invalido!')
