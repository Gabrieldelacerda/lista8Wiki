class BichinhoVirtual:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 50
        self.tedio = 50

    def alimentar(self, quantidade):
        self.fome -= quantidade

    def brincar(self, tempo):
        self.tedio -= tempo

    def mostrarEstado(self):
        print(f"Nome: {self.nome}")
        print(f"Nível de Fome: {self.fome}")
        print(f"Nível de Tédio: {self.tedio}")

bichinho = BichinhoVirtual("Bob la Cerda")

quantidade_comida = int(input("Quanta comida você quer dar ao bichinho? "))
tempo_brincadeira = int(input("Quanto tempo você quer brincar com o bichinho? "))

bichinho.alimentar(quantidade_comida)
bichinho.brincar(tempo_brincadeira)

bichinho.mostrarEstado()
