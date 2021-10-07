idade = soma_idade = media = numero_usuarios = 0
while True:
    idade = int(input('Qual e a sua idade?\nR: '))
    soma_idade += idade
    numero_usuarios += 1
    p = input('Deseja parar o programa e calcular a media?(s/n)')
    if p == 's':
        media = soma_idade / numero_usuarios
        break
if 0 < media < 26:
    print('Turma jovem!')
elif 25 < media < 61:
    print('Turma adulta!')
elif media > 60:
    print('Turma idosa!')