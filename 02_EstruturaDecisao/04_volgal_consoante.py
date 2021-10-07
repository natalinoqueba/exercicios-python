# Programa que verifique se uma letra digitada é vogal ou consoante.

vogais = ('a', 'e', 'u', 'o', 'u') 
letra = str(input('Digite uma letra qualquer: '))
if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print(f'{letra} e uma volgal')
else:
    print(f'{letra} e uma consoante')
