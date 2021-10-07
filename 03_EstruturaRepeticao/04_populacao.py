print('Populaçao do pais A e 80000. Populaçao do pais B e 200000')
pais_a = 80000
pais_b = 200000
percentagem_a = 3
percentagem_b = 1.5
ano = 0
while pais_a < pais_b:
    pais_a += pais_a * percentagem_a
    pais_b += pais_b * percentagem_b
    ano += 1
print(f'Serao necessarios {ano} anos para a populaçao do pais A se igualar ou ultrapassar a populaçao do pais B!')