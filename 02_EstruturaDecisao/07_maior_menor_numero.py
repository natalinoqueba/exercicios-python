#  Programa que leia três números e mostre o maior e o menor deles

n1 = float(input('Digite um numero: '))
n2 = float(input('Digite um outro numero: '))
n3 = float(input('Digite um outro numero: '))
if n1 > n3 > n2:
    print(f'{n1} e o maior numero e {n2} o menor numero.')
elif n2 > n1 > n3:
    print(f'{n2} e o maior numero e {n3} o menor numero.')
else:
    print(f'{n3} e o maior numero e {n1} o menor numero.')
