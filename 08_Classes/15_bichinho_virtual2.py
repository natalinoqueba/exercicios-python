class BichinoVirtual:
    def __init__(self, nome, idade,  fome = 15, saude = 20, humor = 10):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade
        self.humor = humor

    def alt_nome(self, nome):
        self.nome = nome
        print(self.nome)

    def ret_nome(self):
        return self.nome

    def comer(self, quant_comida):
        if self.fome < 0:
            self.fome -= quant_comida

    def alt_saude(self, saude):
        self.saude += saude
        print(self.saude)

    def alt_idade(self, idade):
        self.idade = idade
        print(self.idade)

    def hmor(self):
        self.humor = self.saude - self.fome
        if self.humor >= 10:
            print('Muito feliz')
        elif self.humor < 10:
            print('Feliz')
        elif self.humor < 5:
            print('Triste')

    def brincar(self, tempo):
        if self.humor < 15:
            self.saude += tempo / 2


animal = BichinoVirtual('Lups', 1)
print(animal.ret_nome())
animal.hmor()
animal.comer(10)
animal.alt_saude(6)
animal.brincar(5)
animal.hmor()
