class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def imprimir_pontos(self):
        print(f'Ponto x: {self.x} Ponto y: {self.y}')

    def xy(self):
        return self.x, self.y

class Retangulo():
    def __init__(self, comprimento, largura, ponto):
        self.ponto = ponto
        self.comprimento = comprimento
        self.largura = largura

    def centro_retangulo(self):
        return Ponto(self.comprimento / 2, self.largura / 2)

    def menu(self, comprimento, largura):
        print('Aletrando valores do retangulo')
        self.comprimento = comprimento
        self.largura = largura
        print(f'Centro do retangulo: {r.centro_retangulo().xy()}')


p = Ponto(1, 4)
p.imprimir_pontos()

r = Retangulo(4, 9, p)
print(f'Centro do retangulo: {r.centro_retangulo().xy()}')
r.menu(7, 13)