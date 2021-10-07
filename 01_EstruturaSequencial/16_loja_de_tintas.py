#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta
#é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
#Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

area = float(input('Qual e o tamanho da area a ser pintada(metros quadrados)?\nArea: '))
lata = int(area / 54)
if area % 54 != 0:
    lata += 1
preco = lata * 80.00
print(f'Precisara de {lata} latas, o preço toltal de latas e {preco}MT')