class Macaco:
    def __init__(self, nome, comida='Vazio'):
        self.nome = nome
        self.estomago = comida

    def comer(self, comida):
        if self.estomago == 'Vazio':
            self.estomago = comida
        else:
            self.estomago += f', {comida}'

    def ver_estomago(self):
        print(self.estomago)

    def digeir(self):
        self.estomago = 'Vazio'


m1 = Macaco('Jo')
m2 = Macaco('Ao')

m1.comer('Banana')
m1.ver_estomago()
m1.comer('Maca')
m1.comer('Pera')
m1.ver_estomago()
m1.digeir()
m1.ver_estomago()
print('\n\n')

m2. comer('Castanha')
m2.comer('Laranja')
m2.comer(m1)
m2.ver_estomago()
