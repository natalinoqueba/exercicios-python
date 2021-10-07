nota1 = float(input('1ª nota: '))
nota2 = float(input('2ª nota: '))
media = (nota1+nota2)/2
conceito = ''
ar = ''
if 9.0 < media <= 10.0:
    conceito = 'A'
    ar = 'APROVADO'
elif 7.5 < media <= 9.0:
    conceito = 'B'
    ar = 'APROVADO'
elif 6.0 < media <= 7.5:
    conceito = 'C'
    ar = 'APROVADO'
elif 4.0 < media <= 6.0:
    conceito = 'D'
    ar = 'REPROVADO'
elif 0 <= media <= 4:
    conceito = 'E'
    ar = 'REPROVADO'
print('\n\n')
print('===============================================================')
print('1ª nota      2ª nota     Media de aproveitamento      Conceito')
print(f'{nota1}{nota2:13}{media:13}                         {conceito:10}\n')
print(ar)
print('===============================================================')