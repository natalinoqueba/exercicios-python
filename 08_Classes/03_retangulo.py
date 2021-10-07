class Retangulo:
    comprimento = 5
    largura = 10

    def mudar_valores(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def retornar_valores(self):
        return self.comprimento, self.largura

    def calcular_area(self):
        print(f'Area: {self.comprimento * self.largura}')

    def calcular_perimetro(self):
        print(f'Perimetro: {2*self.comprimento + 2*self.largura}')


ret = Retangulo()
ret.calcular_area()
ret.calcular_perimetro()
print(ret.retornar_valores())
ret.mudar_valores(3, 5)
ret.calcular_perimetro()
