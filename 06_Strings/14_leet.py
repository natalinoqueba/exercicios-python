letras = {'a': '4', 'b': '8', 'c': '(', 'd': '[)', 'e': '3', 'f': 'ph', 'g': '6', 'h': '/-/', 'i': '!', 'j': '_/',
          'k': '|<', 'l': '1_', 'm': '|\/|', 'n': '|\|', 'o': '0', 'p': '9', 'r': '|2', 's': '5', 't': '7', 'u': 'v',
          'w': '\|/', 'x': '><', 'y': '`/', 'z': 'Z'}

pal = ''
palavra = input('Digite uma palavra: ').lower()
for x in range(len(palavra)):
    pal += letras[palavra[x]]
print(pal)
