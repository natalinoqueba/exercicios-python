preco_morango = preco_maca = 0
quantidade_morango = float(input('Quantidade de morangos(em Kg): '))
quantidade_maca = float(input('Quantidade de maça(em Kg): '))
quantidad_total = quantidade_maca + quantidade_morango
if quantidade_morango <= 5:
    preco_morango = quantidade_morango * 2.50
else:
    preco_morango = quantidade_morango * 2.20
if quantidade_maca:
    preco_maca = quantidade_maca * 1.80
else:
    preco_maca = quantidade_maca * 1.50
preco_total = preco_morango + preco_maca
if quantidad_total > 8 or preco_total > 25:
    preco_total = preco_total - (preco_total * 0.1)
print(f'Preço: {preco_total}')
