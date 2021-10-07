combustivel = input('Tipo de combustivel(A - Alcool, G - Gasolina): ')
comb = combustivel.lower()
litros = float(input('Litros do combustivel: '))
valor = valorf = 0
if litros <= 20:
    if comb == 'a':
        valor = litros * 1.90
        valorf = valor - (valor * 0.03)
    elif comb == 'g':
        valor = litros * 2.50
        valorf = valor - (valor * 0.04)
else:
    if comb == 'a':
        valor = litros * 1.90
        valorf = valor - (valor * 0.05)
    elif comb == 'g':
        valor = litros * 2.50
        valorf = valor - (valor * 0.06)
print(f'Preço: {valorf}')
