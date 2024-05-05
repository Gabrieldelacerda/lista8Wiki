import random

class BichinhoVirtual:
    def __init__(self, nome):
        self.nome = nome
        self.fome = random.randint(0, 100)
        self.tedio = random.randint(0, 100)

    def alimentar(self, quantidade):
        self.fome -= quantidade

    def brincar(self, tempo):
        self.tedio -= tempo

    def mostrarEstado(self):
        print(f"Bichinho {self.nome}:")
        print(f"Nível de Fome: {self.fome}")
        print(f"Nível de Tédio: {self.tedio}")

class FazendaBichinhos:
    def __init__(self):
        self.bichinhos = []

    def adicionarBichinho(self, bichinho):
        self.bichinhos.append(bichinho)

    def alimentarTodos(self, quantidade):
        for bichinho in self.bichinhos:
            bichinho.alimentar(quantidade)

    def brincarTodos(self, tempo):
        for bichinho in self.bichinhos:
            bichinho.brincar(tempo)

    def ouvirTodos(self):
        for bichinho in self.bichinhos:
            bichinho.mostrarEstado()

fazenda = FazendaBichinhos()

fazenda.adicionarBichinho(BichinhoVirtual("Bob la Cerda"))
fazenda.adicionarBichinho(BichinhoVirtual("Gaya"))
fazenda.adicionarBichinho(BichinhoVirtual("T-Rex"))

fazenda.alimentarTodos(20)
fazenda.brincarTodos(30)
fazenda.ouvirTodos()
