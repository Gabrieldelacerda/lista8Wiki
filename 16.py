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

    def __str__(self):
        return f"Nome: {self.nome}\nNível de Fome: {self.fome}\nNível de Tédio: {self.tedio}"

bichinho = BichinhoVirtual("Fido")

opcao = input("Escolha uma opção (alimentar / brincar / mostrar): ")

if opcao == "alimentar":
    quantidade_comida = int(input("Quanta comida você quer dar ao bichinho? "))
    bichinho.alimentar(quantidade_comida)
elif opcao == "brincar":
    tempo_brincadeira = int(input("Quanto tempo você quer brincar com o bichinho? "))
    bichinho.brincar(tempo_brincadeira)
elif opcao == "mostrar":
    bichinho.mostrarEstado()
elif opcao == "secreto":
    print(bichinho)
else:
    print("Opção inválida.")
