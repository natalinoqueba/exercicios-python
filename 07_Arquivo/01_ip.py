ips_validos = list()
ips_invalidos = list()
ips = open('ip.txt', 'r')

for i in ips:
    ip = i.replace('\n', '')
    ip = ip.split('.')
    c = 0
    for x in ip:
        c += 1
        if int(x) > 224:
            ip = '.'.join(ip)
            ips_invalidos.append(ip)
            break
        elif c == 4:
            ip = '.'.join(ip)
            ips_validos.append(ip)

ips.close()
saida = open('saida.txt', 'w')
saida.write('[Endereços válidos:]\n')
for y in ips_validos:
    saida.write(f'{y}\n')
saida.write('\n\n[Endereços inválidos:]\n')
for x in ips_invalidos:
    saida.write(f'{x}\n')
