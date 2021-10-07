class Conta:
    def __init__(self, numero_conta, nome, saldo = 0):
        self.numero_conta = numero_conta
        self.nome = nome
        self.saldo = saldo

    def alterar_nome(self, nome):
        self.nome = nome
        print(self.nome)

    def deposito(self, deposito):
        self.saldo += deposito
        print(f'Saldo atual: {self.saldo}')

    def saque(self, saque):
        if saque > self.saldo:
            print('Valor indisponivel na conta')
        else:
            self.saldo -= saque
            print(f'Saldo atual: {self.saldo}')


conta = Conta(12345, 'Jorge')
conta.saque(100)
conta.deposito(200)
conta.saque(100)
conta.alterar_nome('Joana')
