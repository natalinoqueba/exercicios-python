par = list()
impar = list()
nr = list()
for x in range(0, 20):
    nr.append(int(input('Introduza um numero inteiro: ')))
    if nr[x] % 2 == 0:
        par.append(nr[x])
    else:
       impar.append(nr[x])
print(f'{nr}\n{par}\n{impar}')