#m Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido

sexo = str(input('Sexo (F/M): '))
if sexo == 'F' or sexo == 'f':
    print('Feminino')
elif sexo == 'M' or sexo == 'm':
    print('Masculino')
else:
    print('Sexo invalido')
