valores = list()
media = val = 0.0
acimamedia = soma = abaixosete = 0
while True:
    val = int(input('Digite a nota: '))
    if val == -1:
        break
    elif val >= 0:
        valores.append(val)
for x in valores:
    soma += x
    print(f'{x}', end=' ')
print()
for x in range(len(valores) - 1, -1, -1):
    print(valores[x])
media = soma/len(valores)
for x in valores:
    if x > media:
        acimamedia += 1
    if x < 7:
        abaixosete += 1
print(f'Soma dos valores: {soma}\n'
      f'Media dos valores: {media}\n'
      f'Quantidade de valores acima da media: {acimamedia}\n'
      f'Quantidade de valores abaixo de sete: {abaixosete}')
print('*' * 30)
print(' ' * 10 + 'Mensagem')
print('*' * 30)
