class ContaInvestimento:
    def __init__(self, saldo_inicial, taxa_juros):
        self.saldo = saldo_inicial
        self.taxa_juros = taxa_juros / 100

    def adicioneJuros(self):
        self.saldo += self.saldo * self.taxa_juros

poupanca = ContaInvestimento(1000, 10)

for _ in range(5):
    poupanca.adicioneJuros()

print("Saldo após aplicar juros cinco vezes:", poupanca.saldo)
