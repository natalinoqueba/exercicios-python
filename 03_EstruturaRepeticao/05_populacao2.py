repetir = True
while repetir:
    pais_a = int(input('Populacao do pais A: '))
    pais_b = int(input('Populacao do pais B: '))
    percentagem_a = float(input('Taxa de crescimento do pais A: '))
    percentagem_b = float(input('Taxa de crescimento do pais B: '))
    ano = 0
    print(f'Populaçao do pais A e {pais_a}. Populaçao do pais B e {pais_b}')
    if pais_a < pais_b:
        while pais_a < pais_b:
            pais_a += pais_a * percentagem_a
            pais_b += pais_b * percentagem_b
            ano += 1
        print(f'Serao necessarios {ano} anos para a populaçao do pais A se igualar ou ultrapassar a populaçao do pais B!')
    else:
        while pais_b < pais_a:
            pais_a += pais_a * percentagem_a
            pais_b += pais_b * percentagem_b
            ano += 1
        print(f'Serao necessarios {ano} anos para a populaçao do pais B se igualar ou ultrapassar a populaçao do pais A!')
    r = input('Deseja repetir?(S/N)\nR:')
    if r.lower() == 's':
        repetir = True
    else:
        repetir = False