def valor_pagamento(prestacao, atraso):
    if atraso > 0:
        valor_pagar = prestacao + prestacao * 0.03 + (prestacao * 0.01) * atraso
    else:
        valor_pagar = prestacao
    return valor_pagar

valor_total = quantidade = 0
while True:
    val = float(input('Valor da prestacao: '))
    if val == 0:
        break
    valor = valor_pagamento(val, int(input('Dias em atraso = ')))
    print(f'O valora a pagar da prestacao e: {valor:.2f}')
    valor_total += valor
    quantidade += 1
print(f'\n\nQuantidade de prestacoes pagas hoje: {quantidade}\nValor de prestacoes pagas hoje: {valor_total:.2f}')
