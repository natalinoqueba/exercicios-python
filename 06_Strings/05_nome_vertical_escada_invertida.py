st = input('Nome: ')
st = st.upper()

for x in range(len(st), -1, -1):
    for y in range(0, x):
        print(st[y], end='')
    print('')
