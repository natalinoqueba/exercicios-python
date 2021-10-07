lata = 0
galao = 0
preco_lata = int
preco_galao = int
area = float(input('Qual e o tamanho da area a ser pintada(metros quadrados)?\nArea: '))
area_lata = 108.0  # area em metros quadrados por cada lata
area_galao = 21.6  # area em metros quadrados por cada galao
if area >= area_lata:
    lata = int(area / area_lata)
    if area % area_lata != 0:
        x = area - (lata * area_lata)  # X - variavel usada para verificar se sera aumentada a quantidade de tinta
        # com galoes ou com latas
        if x > area_galao * 3:  # se x for maior que 64,8 que e equivalente a 75 mt sera adquirida uma lata que saira
            # a 80 mt porque que mais um galao custara 100 mt
            lata += 1
        else:  # x menor que 64,8
            galao = int(x / area_galao)
            if x % area_galao != 0:
                galao += 1
else:
    if area > area_galao * 3:
        lata += 1
    else:
        galao = int(area / area_galao)
        if area % area_galao != 0:
            galao += 1
preco_galao = galao * 25
preco_lata = lata * 80
preco_total = preco_lata + preco_galao
print('\nArea a pintar    Lata    Galao    Preço total')
print(f'{area:} {lata:12} {galao:8} {preco_total:8}')
