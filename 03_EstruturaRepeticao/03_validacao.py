print('Validacao    || Sexo(f - femenino, m -  masculino) Estado civil(s - solteiro, c - casad0, v - viuvo, d - divorciado)')
nome = input('Nome: ')
idade = int(input('Idade: '))
salario = float(input('Salario: '))
sexo = input('Sexo: ')
sex = ('f', 'm')
estadocivil = input('Estado civil: ')
estado = ('s', 'c', 'v', 'd')
while len(nome) <= 3 or idade > 150 or idade < 0 or salario < 0 or sexo not in sex or estadocivil not in estado:
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    salario = float(input('Salario: '))
    sexo = input('Sexo: ')
    sex = ('f', 'm')
    estadocivil = input('Estado civil: ')
    estado = ('s', 'c', 'v', 'd')