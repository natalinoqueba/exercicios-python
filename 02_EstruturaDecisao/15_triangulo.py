while True:
    print('Os lados formam triangulo?\n')
    lado1 = float(input('Lado 1 : '))
    lado2 = float(input('Lado 2 : '))
    lado3 = float(input('Lado 3 : '))
    soma1 = lado2 + lado3
    soma2 = lado1 + lado3
    soma3 = lado1 + lado2
    if soma1 > lado1 and soma2 > lado2 and soma3 > lado3:
        if lado1 == lado2 == lado3:
            print('Triangulo Equilatero')
        elif lado1 == lado2 != lado3 or lado1 == lado3 != lado2 or lado3 == lado2 != lado1:
            print('Triangulo Isosceles')
        else:
            print('Triangulo escaleno')
    else:
        print('Os lados nao podem formar um triangulo!')
