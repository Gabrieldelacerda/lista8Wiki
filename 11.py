class Carro:
    def __init__(self, consumo):
        self.consumo = consumo
        self.combustivel = 0

    def andar(self, distancia):
        combustivel_necessario = distancia / self.consumo
        if combustivel_necessario <= self.combustivel:
            self.combustivel -= combustivel_necessario
            print(f"O carro andou {distancia} km.")
        else:
            print("Não há combustível suficiente para percorrer essa distância.")

    def obterGasolina(self):
        return self.combustivel

    def adicionarGasolina(self, litros):
        self.combustivel += litros

minhaFerrari = Carro(15)
minhaFerrari.adicionarGasolina(20)
minhaFerrari.andar(100)
print("Combustível restante:", minhaFerrari.obterGasolina(), "litros")
