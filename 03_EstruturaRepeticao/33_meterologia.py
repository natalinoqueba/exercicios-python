tempma = tempme = mtemp = s = 0
while True:
    temp = float(input('Temperatura: '))
    if temp > tempma:
        tempma = temp
    if tempme == 0:
        tempme = temp
    elif temp < tempme:
        tempme = temp
    s += 1
    mtemp += temp
    if input('S - Parar / N - Continuar: ') == 's':
        break
print(f'Temeratura maior: {tempma}\nTemperatura menor: {tempme}\nMedia temperatura: {mtemp/s}')
