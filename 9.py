class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def imprimir(self):
        print(f"Ponto: ({self.x}, {self.y})")


class Retangulo:
    def __init__(self, ponto_inicial, largura, altura):
        self.ponto_inicial = ponto_inicial
        self.largura = largura
        self.altura = altura

    def encontrar_centro(self):
        centro_x = self.ponto_inicial.x + self.largura / 2
        centro_y = self.ponto_inicial.y + self.altura / 2
        return Ponto(centro_x, centro_y)


def menu():
    print("\n===== Menu =====")
    print("1. Alterar valores do retângulo")
    print("2. Imprimir centro do retângulo")
    print("3. Sair")

ponto_partida = Ponto(1, 1)
retangulo1 = Retangulo(ponto_partida, 5, 3)
retangulo2 = Retangulo(Ponto(3, 3), 4, 2)

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        x = int(input("Digite a coordenada x do ponto inicial: "))
        y = int(input("Digite a coordenada y do ponto inicial: "))
        largura = int(input("Digite a largura do retângulo: "))
        altura = int(input("Digite a altura do retângulo: "))

        ponto_partida = Ponto(x, y)
        retangulo1 = Retangulo(ponto_partida, largura, altura)
    elif opcao == '2':
        centro = retangulo1.encontrar_centro()
        centro.imprimir()
    elif opcao == '3':
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")
