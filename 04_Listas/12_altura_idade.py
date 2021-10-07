idade = list()
altura = list()
medialt = 0.0
abaixomedia = 0
for x in range(0, 5):
    idade.append(int(input('Idade do aluno: ')))
    altura.append(float(input('Altura do aluno: ')))
for y in altura:
    medialt += y
medialt = medialt/5
for x in range(0, 5):
    if idade[x] > 13 and altura[x] < medialt:
        abaixomedia += 1
print(f'Media das alturas: {medialt:.2f}\nNumero de alunos acima de 13 anos com a altura menor que a media: {abaixomedia}')
