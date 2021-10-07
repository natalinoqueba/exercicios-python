class Quadrado:
    tamanho_lado = 8

    def mudar_valor_lado(self, valor):
        self.tamanho_lado = valor

    def retornar_valor(self):
        return self.tamanho_lado

    def calcular_area(self):
        print(self.tamanho_lado**2)


q = Quadrado()
q.calcular_area()
print(f'Valor da area: {q.retornar_valor()}')
q.mudar_valor_lado(5)
q.calcular_area()
