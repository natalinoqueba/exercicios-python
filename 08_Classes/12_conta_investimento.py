class ContaInvestimento:
        def __init__(self, numero_conta, nome, taxa_juros, saldo):
            self.numero_conta = numero_conta
            self.nome = nome
            self.saldo = saldo
            self.taxa_juros = taxa_juros

        def alterar_nome(self, nome):
            self.nome = nome
            print(self.nome)

        def deposito(self, deposito):
            self.saldo += deposito
            print(f'Saldo atual: {self.saldo}')


        def adicione_juros(self):
            self.saldo += self.saldo * (self.taxa_juros / 100)
            print(f'{self.saldo:.2f}')


poupanca = ContaInvestimento(341441, 'Benny', 10, 1000)
for x in range(0, 5):
    poupanca.adicione_juros()
