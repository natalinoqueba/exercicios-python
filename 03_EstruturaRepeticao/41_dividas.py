qd = 1  # quantidade de parcela
j = vdx = 0  # juros
vd = float(input('Valor da divida: '))
vj = vd * (j / 100)  # valor dos juros
vp = vd / qd  # valor das parcelas
print('Valor da divida     Valor dos juros     Quanditade de parcelas      Valor da parcela')
print(f'{vd}    {int(vj)}    {qd}    {vp:.2f}')
j = 5
for qd in range(3, 13, 3):
    j += 5
    vj = (vd * j) / 100
    vp = vd / qd
    vdx = vd + vj
    print(f'{vdx}    {int(vj)}    {qd}    {vp:.2f}')
