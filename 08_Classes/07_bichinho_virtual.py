class BichinoVirtual:
    def __init__(self, nome, idade,  fome = 0, saude = 10, humor = 'Feliz'):
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

    def alt_fome(self,):
        self.fome += 1
        print(self.fome)

    def alt_saude(self, saude):
        self.saude = saude
        print(self.saude)

    def alt_idade(self, idade):
        self.idade = idade
        print(self.idade)

    def hmor(self):
        if self.saude - self.fome >= 10:
            self.humor = 'Muito Feliz'
        elif 5 < self.fome + self.saude < 10:
            self.humor = 'Feliz'
        elif 0 < self.fome + self.saude < 5:
            self.humor = 'Triste'
        print(self.humor)


animal = BichinoVirtual('Lups', 1)
print(animal.ret_nome())
animal.alt_nome('Lupn')
animal.alt_idade(3)
animal.hmor()
animal.alt_fome()
animal.alt_saude(6)
