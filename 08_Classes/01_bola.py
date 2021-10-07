class Bola:
    cor = 'Azul'
    circunferencia = 5
    material = 'Plastico'

    def troca_cor(self, cor):
        self.cor = cor

    def mostra_cor(self):
        print(self.cor)


b = Bola()
b.mostra_cor()
b.troca_cor('Branca')
b.mostra_cor()
