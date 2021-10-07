class BombaCombustivel:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel

    def abastecer_por_valor(self, valor):
        print(f'Quantidade abastecida no veiculo: {valor / self.valor_litro:.1f}L')
        self.quantidade_combustivel -= valor / self.valor_litro

    def abastecer_por_litro(self, litro):
        print(f'Quantidade abastecida no veiculo: {litro * self.valor_litro} MZN')
        self.quantidade_combustivel -= litro * self.valor_litro

    def alterar_valor(self, valor):
        self.valor_litro = valor

    def alterar_combustivel(self, combustivel):
        self.tipo_combustivel = combustivel
        print(self.tipo_combustivel)

    def alterar_quantidade_combustive(self, quantidade):
        self.quantidade_combustivel = quantidade


combustivel = BombaCombustivel('Gasolina', 100, 500)
combustivel.abastecer_por_valor(200)
combustivel.abastecer_por_litro(3)
combustivel.alterar_valor(150)
combustivel.abastecer_por_valor(100)
combustivel.abastecer_por_litro(1)
combustivel.alterar_combustivel('Disel')
combustivel.alterar_quantidade_combustive(600)
