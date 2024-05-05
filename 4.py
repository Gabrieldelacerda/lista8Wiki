class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos):
        self.idade += anos
        if self.idade < 21:
            self.crescer(0.5 * anos)

    def engordar(self, ganho_de_peso):
        self.peso += ganho_de_peso

    def emagrecer(self, perda_de_peso):
        self.peso -= perda_de_peso

    def crescer(self, ganho_de_altura):
        self.altura += ganho_de_altura

pessoa1 = Pessoa(nome="Gabriel de la Cerda", idade=18, peso=80, altura=183)
print("Altura inicial:", pessoa1.altura)
print("Idade inicial:", pessoa1.idade)

pessoa1.envelhecer(2)
print("Altura após envelhecer:", pessoa1.altura)
print("Idade após envelhecer:", pessoa1.idade)

pessoa1.engordar(5)
print("Peso após engordar:", pessoa1.peso)

pessoa1.emagrecer(3)
print("Peso após emagrecer:", pessoa1.peso)
