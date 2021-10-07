preco = 0.18
print('=' * 40)
print('Preço do pão: R$ 0.18')
print('Panificadora Pão de Ontem - Tabela de preços')
for p in range(1, 51):
    print(f'{p:2} - {p * preco:.2f} Mzn')
print('=' * 40)