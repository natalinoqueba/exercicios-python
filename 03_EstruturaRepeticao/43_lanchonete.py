print('Especificação    Código  Preço\n'
      'Cachorro Quente    100    R$ 1,20\n'
      'Bauru Simples      101    R$ 1,30\n'
      'Bauru com ovo      102    R$ 1,50\n'
      'Hambúrguer         103    R$ 1,20\n'
      'Cheeseburguer      104    R$ 1,30\n'
      'Refrigerante       105    R$ 1,00\n\n\n')
ped = 1
quant = valor1 = total = valor2 = valor3 = valor4 = valor5 = valor6 = 0
while ped == 1:
    pedido = int(input('Codigo do pedido(2 - Encerrar): '))
    if pedido == 2:
        break
    elif pedido < 100 or pedido > 105:
        pedido = int(input('Codigo do pedido(2 - Encerrar): '))
    quant = int(input('Quantidade do pedido'))
    if pedido == 100:
        valor1 = quant * 1.20
        total += valor1
    elif pedido == 101:
        valor2 = quant * 1.30
        total += valor2
    elif pedido == 102:
        valor3 = quant * 1.50
        total += valor3
    elif pedido == 103:
        valor4 = quant * 1.20
        total += valor4
    elif pedido == 104:
        valor5 = quant * 1.30
        total += valor5
    elif pedido == 105:
        valor6 = quant * 1.00
        total += valor6
print('Especificação        Preço')
if valor1 > 0:
    print(f'Cachorro Quente         {valor1}')
if valor2 > 0:
    print(f'Bauru Simples           {valor2}')
if valor3 > 0:
    print(f'Bauru com ovo           {valor3}')
if valor4 > 0:
    print(f'Hambúrguer              {valor4}')
if valor5 > 0:
    print(f'Cheeseburguer           {valor5}')
if valor6 > 0:
    print(f'Refrigerante           {valor6}')
print(f'Total            {total}')
