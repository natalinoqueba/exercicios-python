#  programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato

produto1 = float(input('Preço do primeiro produto: '))
produto2 = float(input('Preço do segundo produto: '))
produto3 = float(input('Preço do terceiro produto: '))
if produto1 < produto2 and produto1 < produto3:
    print(f'Voce deve comprar o primeiro produto!')
elif produto2 < produto1 and produto2 < produto3:
    print(f'Voce deve comprar o segundo produto!')
else:
    print(f'Voce deve comprar o terceiro produto!')
