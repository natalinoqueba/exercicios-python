nr = 0
intervalo1 = intervalo2 = intervalo3 = intervalo4 = 0 # intervalos(1 - [0-25]; 2 - [26-50]; 3 - [51-75]; 4 -  [76-100])
while nr >= 0:
    nr = int(input('Digite um numero: '))
    if 0 <= nr <= 25:
        intervalo1 += 1
    elif 26 <= nr <= 50:
        intervalo2 += 1
    elif 51 <= nr <= 75:
        intervalo3 += 1
    elif 76 <= nr <= 100:
        intervalo4 += 1
print(f'{intervalo1} nrs no internalo de 0 a 25\n{intervalo2} nrs no internalo de 26 a 50')
print(f'{intervalo3} nrs no internalo de 51 a 75\n{intervalo4} nrs no internalo de 76 a 100')