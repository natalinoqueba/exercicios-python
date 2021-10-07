class Carro:
    def __init__(self, consumo, combustivel = 0):
        self.consumo = consumo
        self.combustivel = combustivel

    def andar(self, distancia):
        self.combustivel -= distancia / self.consumo

    def obter_gasolina(self):
        print(f'{self.combustivel:.2f}')

    def adicionar_gasolina(self, gasolina):
        self.combustivel += gasolina


carro1 = Carro(15)
carro1.obter_gasolina()
carro1.adicionar_gasolina(20)
carro1.andar(100)
carro1.obter_gasolina()