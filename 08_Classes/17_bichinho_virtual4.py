class BichinoVirtual:
    def __init__(self, nome, idade,  fome , saude, humor = 10):
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
        for x in range(0, quant_comida):
            if self.fome > 0:
                self.fome -= 1

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
        elif 5 < self.humor < 10:
            print('Feliz')
        elif self.humor < 5:
            print('Triste')

    def brincar(self, tempo):
        for x in range(0, tempo):
            if self.humor < 15:
                self.saude += 1

    def __str__(self):
        return  (f'Nome: {self.nome}'
                 f'Idade: {self.idade}'
                 f'\nFome: {self.fome}'
                 f'\nSaude: {self.saude}'
                 f'\nIdade: {self.idade}'
                 f'\nHumor: {self.humor}')


animal2 = BichinoVirtual('Lups', 1, 10, 4, 4)
animal3 = BichinoVirtual('Fern', 2, 5, 5)
animal4 = BichinoVirtual('Jup', 1, 15, 11, 3)
animal5 = BichinoVirtual('Lil', 3, 11, 12, 13)
animal6 = BichinoVirtual('Carl', 4, 1, 6, 8)

fazenda = [animal2, animal3, animal4, animal5, animal6]

for an in fazenda:
    print()
    an.hmor()
for an in fazenda:
    an.brincar(10)
for an in fazenda:
    an.comer(10)
for an in fazenda:
    print()
    an.hmor()
print()
for an in fazenda:
    print()
    print(an)

