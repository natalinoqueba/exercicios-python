def soma_imposto(taxa_imposto, custo):
    custo += custo * (taxa_imposto/100)
    print(f'\nCusto do produto depois do imposto: {custo}')


soma_imposto(float(input('Porcentagem da quantia de imposto sobre vendas: ')), float(input('Custo do produto antes do imposto: ')))
