class BombaCombustivel:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel

    def abastecerPorValor(self, valor_abastecido):
        litros_abastecidos = valor_abastecido / self.valor_litro
        if litros_abastecidos <= self.quantidade_combustivel:
            self.quantidade_combustivel -= litros_abastecidos
            print(f"Foram abastecidos {litros_abastecidos:.2f} litros de {self.tipo_combustivel}.")
        else:
            print("Não há combustível suficiente na bomba.")

    def abastecerPorLitro(self, litros_abastecidos):
        valor_pagar = litros_abastecidos * self.valor_litro
        if litros_abastecidos <= self.quantidade_combustivel:
            self.quantidade_combustivel -= litros_abastecidos
            print(f"Valor a pagar: R${valor_pagar:.2f}")
        else:
            print("Não há combustível suficiente na bomba.")

    def alterarValor(self, novo_valor):
        self.valor_litro = novo_valor

    def alterarCombustivel(self, novo_combustivel):
        self.tipo_combustivel = novo_combustivel

    def alterarQuantidadeCombustivel(self, nova_quantidade):
        self.quantidade_combustivel = nova_quantidade

    def __str__(self):
        return (f"Tipo de combustível: {self.tipo_combustivel}\nValor por litro: R${self.valor_litro:.2f}\nQuantidade "
                f"de combustível na bomba: {self.quantidade_combustivel:.2f} litros")

bomba1 = BombaCombustivel("Gasolina", 5.0, 1000)
print(bomba1)

bomba1.abastecerPorValor(50)
print(bomba1)

bomba1.abastecerPorLitro(20)
print(bomba1)

bomba1.alterarValor(5.5)
bomba1.alterarCombustivel("Diesel")
bomba1.alterarQuantidadeCombustivel(1500)
print(bomba1)
