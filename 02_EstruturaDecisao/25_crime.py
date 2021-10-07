culpa = 0
print('Respondas as questoes com "Sim" e "Nao"')
perg1 = input('Telefonou para a vitima?\nR: ')
r1 = perg1.lower()
if r1 == 'sim':
    culpa += 1
perg2 = input('Esteve no local do crime??\nR: ')
r2 = perg2.lower()
if r2 == 'sim':
    culpa += 1
perg3 = input('Mora perto da vitima?\nR: ')
r3 = perg3.lower()
if r3 == 'sim':
    culpa += 1
perg4 = input('Devia para a vitima?\nR: ')
r4 = perg4.lower()
if r4 == 'sim':
    culpa += 1
perg5 = input('Ja tarbalhou com a vitima?\nR: ')
r5 = perg5.lower()
if r5 == 'sim':
    culpa += 1
if culpa == 2:
    print('Supeita!')
elif 5 > culpa > 2:
    print('Cumplice!')
elif culpa == 5:
    print('Assassino!')
else:
    print('Inocente!')
