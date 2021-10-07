valorcd = totalcd = 0
quantidadecd = int(input('Quantidade de CDS: '))
for cd in range(1, quantidadecd + 1):
    valorcd = float(input(f'Valor do {cd} CD: '))
    totalcd += valorcd
md = totalcd / quantidadecd
print(f'Valor total gasto: {totalcd}    Valor medio por cada CD: {md}')
