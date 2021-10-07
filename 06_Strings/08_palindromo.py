st = input('Frase qualquer: ')

sti = st.upper()
nova = sti.split()
nova = ''.join(nova)
outra = nova[::-1]
if outra == nova:
    print(f'A frase {st} e um palindromo!'
          f'\n{nova} == {outra}')
else:
    print(f'A frase {st} nao e um palindromo!'
          f'\n{nova} != {outra}')
