nota1 = float(input('1ª Nota: '))
nota2 = float(input('2ª Nota: '))
nota3 = float(input('3ª Nota: '))
media = (nota1 + nota2 + nota1) / 3
if media == 10:
    print(f'Media : {media}')
    print("Aprovado com Distinção")
elif media >= 7:
    print(f'Media : {media}')
    print("Aprovado")
elif media < 7:
    print(f'Media : {media}')
    print("Reprovado")
