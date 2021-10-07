numa= num = soma = nume= 0
while True:
    num = int(input('Digite um numero(de 0 a 1000): '))
    if 0 > num < 1000:
        print('So numeros maiores que zero e menores que 1000!')
        break
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
