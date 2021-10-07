class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, idade):
        if self.idade < 21:
            self.altura += 0.05 * (idade - self.idade)
            print(f'Altura: {self.altura}')
        self.idade = idade
        print(f'Idade: {self.idade}')

    def engordar(self, peso):
        self.peso += peso
        print(f'Peso: {self.peso}')

    def emagrecer(self, peso):
        self.peso -= peso
        print(f'Peso: {self.peso}')

    def crescer(self, altura):
        self.altura += altura
        print(f'Altura: {self.altura}')


pessoa = Pessoa('Jorge', 17, 36, 1.5)
pessoa.envelhecer(18)
pessoa.engordar(40)
pessoa.emagrecer(35)
pessoa.crescer(1.7)
