class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def detalhes_funcionario(self):
        print(f'\nNome: {self.nome}\nSalario: {self.salario}')


func1 = Funcionario('Jorge', 1000)
func2 = Funcionario('Abreu', 2000)
func1.detalhes_funcionario()
func2.detalhes_funcionario()