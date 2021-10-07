preco1 = preco2 = quantidade2 = desconto = preco_desconto= carne2 = 0
tipo1 = tipo2 = ''
c2 = False
print('Promoçao de carnes no Tabajara!!(Apenas dois tipos de carne por cliente)')
print('1 - File duplo\n2 - Alcatra\n3 - Picanha\n')
carne1 = int(input('Tipo de carne desejado: '))
quantidade1 = float(input('Quantidade(kg): '))
deseja = input('Deseja levar outro tipo de carne? (S/N)')
if deseja.lower() == 's':
    c2 = True
    carne2 = int(input('Tipo de carne desejado: '))
    quantidade2 = float(input('Quantidade(kg): '))
if carne1 == 1:
    tipo1 = 'File Duplo'
    if quantidade1 <= 5:
        preco1 = quantidade1 * 4.90
    else:
        preco1 = quantidade1 * 5.80
elif carne1 == 2:
    tipo1 = 'Alcatra'
    if quantidade1 <= 5:
        preco1 = quantidade1 * 5.90
    else:
        preco1 = quantidade1 * 6.80
elif carne1 == 3:
    if quantidade1 <= 5:
        tipo1 = 'Picanha'
        preco1 = quantidade1 * 6.90
    else:
        tipo1 = 'Picanha'
        preco1 = quantidade1 * 7.80
if carne2 == 1:
    tipo2 = 'File Duplo'
    if quantidade1 <= 5:
        tipo2 = 'File Duplo'
        preco2 = quantidade1 * 4.90
    else:
        preco2 = quantidade1 * 5.80
elif carne2 == 2:
    tipo2 = 'Alcatra'
    if quantidade1 <= 5:
        preco2 = quantidade1 * 5.90
    else:
        preco2 = quantidade1 * 6.80
elif carne2 == 3:
    tipo2 = 'Picanha'
    if quantidade1 <= 5:
        preco2 = quantidade1 * 6.90
    else:
        preco2 = quantidade1 * 7.80
preco_total = preco1 + preco2
cartao_tabajara = input('Cartao Tabajara(S/N): ')
cartao = 'Dinheiro'
if cartao_tabajara.lower() == 's':
    cartao = 'Cartao Tabajara'
    desconto = preco_total * 0.05
    preco_desconto = preco_total - desconto
else:
    preco_desconto = preco_total
print('\n')
print('»' * 35)
print('CUPOM FISCAL\n')
print('               Quantidade      Preço\n')
print(f'{tipo1:15} {quantidade1:8} {preco1:11}')
if c2:
    print(f'{tipo2:15} {quantidade2:8} {preco2:11}')
print(f'\n\nPreço total {preco_total:24}')
print(f'Forma de pagamento   {cartao:22}')
if cartao == 'Cartao Tabajara':
    print(f'Desconto' + ' ' * 23 + f'{desconto:.2f}')
print(f'Valor a pagar' + ' ' * 17 + f'{preco_desconto:.2f}')
print('«' * 35)
