st = input('Frase qualquer: ')

esp = st.count(' ')
a = st.count('a')
e = st.count('e')
i = st.count('i')
o = st.count('o')
u = st.count('u')

print(f'Existem {esp} espacos em branco na frase;'
      f'Existem {a + e + i + o + u} vogais na frase.')