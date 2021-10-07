numa = soma = nume= 0
while True:
    num = int(input('Digite um numero: '))
    soma += num
    if numa == nume == 0:
        numa = num
        nume = num
    if num > numa:
        numa = num
    elif num < nume:
        nume = num
    terminar = input('Deseja terminar? (s/n): ')
    if terminar == 's':
        print(f'Maior numero: {numa}; Menor numero: {nume}; Soma dos numeros: {soma}')
        break
