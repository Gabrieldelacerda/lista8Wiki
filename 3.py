class Retangulo:
    def __init__(self, lado_a, lado_b):
        self.lado_a = lado_a
        self.lado_b = lado_b

    def mudarLados(self, novo_lado_a, novo_lado_b):
        self.lado_a = novo_lado_a
        self.lado_b = novo_lado_b

    def retornarLados(self):
        return self.lado_a, self.lado_b

    def calcularArea(self):
        return self.lado_a * self.lado_b

    def calcularPerimetro(self):
        return 2 * (self.lado_a + self.lado_b)

def calcular_pisos_rodapes(local):
    tamanho_piso = 1
    tamanho_rodape = 0.1
    area_local = local.calcularArea()
    perimetro_local = local.calcularPerimetro()

    quantidade_pisos = area_local /  tamanho_piso
    quantidade_rodapes = perimetro_local * tamanho_rodape

    return quantidade_pisos, quantidade_rodapes

comprimento = float(input("Informe o comprimento do local: "))
largura = float(input("Informe a largura do local: "))

local = Retangulo(comprimento, largura)

pisos, rodapes = calcular_pisos_rodapes(local)

print("Quantidade de pisos necessários:", pisos)
print("Quantidade de rodapés necessários:", rodapes)
