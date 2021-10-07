menoralt = menorpes = 100
maiorpes = maioralt = speso = saltura = soma = codpesmaior = codaltmaior = codaltmenor = codpesmenor = 0
while True:
    cod = int(input('Codigo: '))
    if cod == 0:
        break
    alt = float(input('Altura(m): '))
    pes = float(input('Peso(kg): '))
    saltura += alt
    speso += pes
    if alt > maioralt:
        maioralt = alt
        codaltmaior = cod
    if alt < menoralt:
        menoralt = alt
        codaltmenor = cod
    if pes > maiorpes:
        maiorpes = pes
        codpesmaior = cod
    if pes < menorpes:
        menorpes = pes
        codpesmenor = cod
    soma += 1
mediaalt = saltura / soma
mediapes = speso / soma
print('Atrinuto     Codigo')
print(f'Altura maior: {codaltmaior:3}')
print(f'Altura menor: {codaltmenor:3}')
print(f'Peso maior: {codpesmaior:5}')
print(f'Peso menor:{codpesmenor:6}')
print('')
print(f'Media(Altura): {mediaalt:.3f}')
print(f'Media(Peso) {mediapes:.3f}')