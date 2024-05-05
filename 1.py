class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, nova_cor):
        self.cor = nova_cor

    def mostraCor(self):
        print("A cor da bola é:", self.cor)

minha_bola = Bola(cor="vermelha", circunferencia=10, material="plástico")
minha_bola.mostraCor()
minha_bola.trocaCor("azul")
minha_bola.mostraCor()
