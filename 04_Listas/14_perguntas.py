perguntas = ('Telefonou para a vítima? ', 'Esteve no local do crime? ', 'Mora perto da vítima? ', 'Devia para a vítima? ', 'Já trabalhou com a vítima? ')
resp = 0
print('Reponda com "SIM" ou "NAO"')
for pergunta in perguntas:
    if input(pergunta) == 'SIM':
        resp += 1
if resp == 2:
    print('Suspeito')
elif 5 > resp > 1:
    print('Cumplice')
elif resp == 5:
    print('Assassino')
else:
    print('Inocente')


