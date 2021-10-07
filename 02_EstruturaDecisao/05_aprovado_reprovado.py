# programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
# mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# mensagem "Reprovado", se a média for menor do que sete
# mensagem "Aprovado com Distinção", se a média for igual a dez.


nota1 = float(input('1ª Nota: '))
nota2 = float(input('2ª Nota: '))
media = (nota1 + nota2)/2
if media == 10:
    print("Aprovado com Distinção")
elif media >= 7:
    print("Aprovado")
else:
    print("Reprovado")
