# Programa que leia três números e mostre o maior deles

n1 = float(input('Digite um numero: '))
n2 = float(input('Digite um outro numero: '))
n3 = float(input('Digite um outro numero: '))
if n1>n2 and n1>n3:
    print(f'{n1} e o maior numero.')
elif n2>n1 and n2>n3:
    print(f'{n2} e o maior numero.')
else:
    print(f'{n3} e o maior numero.')
