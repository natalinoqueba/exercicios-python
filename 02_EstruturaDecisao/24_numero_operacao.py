num1 = float(input('Digite um numero: '))
num2 = float(input('Digite outro numero: '))
print('1 - Multiplicaçao  2 - Divisao  3 - Adiçao  4 Subtraçao')
res = 0
op = int(input('Que operaçao deseja realizar?\nR: '))
if op == 1:
    res = num1 * num2
elif op == 2:
    res = num1 / num2
elif op == 3:
    res = num1 + num2
elif op == 4:
    res = num1 - num2
inteiro = ""
if res == int(res):
    inteiro = 'inteiro'
else:
    inteiro = 'decimal'
par = ''
if res % 2 == 0:
    par = 'par'
else:
    par = 'impar'
postivo = ''
if res >= 0:
    postivo = 'positivo'
else:
    postivo = 'negativo'
print(f'O resultado e {res}! O numero e {par}, {postivo} e {inteiro}')
