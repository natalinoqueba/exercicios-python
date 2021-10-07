print('"ATM"')
print('Valor minimo: 10 | Valor maximo: 600\n')
valor = int(input('Valor a levantar: '))
nota100 = nota50 = nota10 = nota5 = nota1 = 0
if 10 <= valor <= 600:
    nota100 = int(valor / 100)
    if valor % 100 != 0:
        v1 = valor - (nota100 * 100)
        nota50 = int(v1 / 50)
        if v1 % 50 != 0:
            v2 = v1 - (nota50 * 50)
            nota10 = int(v2 / 10)
            if v2 % 10 != 0:
                v3 = v2 - (nota10 * 10)
                nota5 = int(v3 / 5)
                if v3 % 5 != 0:
                    v4 = v3 - (nota5 * 5)
                    nota1 = int(v4 / 1)
print('Nota(100):      Nota(50):      Nota(10):      Nota(5):      Nota(1):')
print(f'{nota100:10}{nota50:15}{nota10:16}{nota5:15}{nota1:13}')
