nrmenor = menor2000 = cidademenor = cidademaior= maioracidente = menoracidente = somaveiculos = 0
for cidade in range(1, 6):
    codcidade = input('Codigo da cidade: ')
    numveiculos = int(input('Numero de veiculos da passeio da cidade(em 1999): '))
    numacidentes = int(input('Numero de acidentes de transito com vitimas(em 1999): '))
    if numacidentes > maioracidente:
        maioracidente = numacidentes
        cidademaior = codcidade
    if menoracidente == 0:
        menoracidente = numacidentes
    elif numacidentes < menoracidente:
        menoracidente = numacidentes
        cidademenor = codcidade
    if numveiculos < 2000:
        menor2000 += numacidentes
        nrmenor += 1
    somaveiculos += numveiculos
mediaveiculos = somaveiculos / 5
mediaacidente = menor2000/nrmenor
print(f'Maior indice de acidente de transito: {maioracidente} - Codigo da cidade: {cidademaior}')
print(f'Menor indidce de acidente de transito: {menoracidente} - Codigo da cidade: {cidademenor}')
print(f'Media de veiculos nas cinco cidades juntas: {mediaveiculos}')
print(f'Media de acidentes de transito nas cidades com menos de 2000 veiculos de passeio: {mediaacidente}')