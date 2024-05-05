class ContaCorrente:
    def __init__(self, numero_conta, nome_correntista, saldo=0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    def alterarNome(self, novo_nome):
        self.nome_correntista = novo_nome

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print("Saque de R$%.2f realizado com sucesso." % valor)
        else:
            print("Saldo insuficiente para a realização do saque.")

conta1 = ContaCorrente(numero_conta="123456", nome_correntista="Gabriel de la Cerda")
print("Saldo inicial:", conta1.saldo)

conta1.deposito(1000)
print("Saldo após depósito:", conta1.saldo)

conta1.saque(500)
print("Saldo após saque:", conta1.saldo)

conta1.alterarNome("Gabriel Preihsner")
print("Novo nome do correntista:", conta1.nome_correntista)
