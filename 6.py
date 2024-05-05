class TV:
    def __init__(self):
        self.canal = 1
        self.volume = 50

    def mudar_canal(self, novo_canal):
        if 1 <= novo_canal <= 100:
            self.canal = novo_canal
            print("Canal alterado para", novo_canal)
        else:
            print("Canal inválido.")

    def aumentar_volume(self):
        if self.volume < 100:
            self.volume += 1
            print("Volume aumentado para", self.volume)
        else:
            print("Volume máximo alcançado.")

    def diminuir_volume(self):
        if self.volume > 0:
            self.volume -= 1
            print("Volume diminuído para", self.volume)
        else:
            print("Volume mínimo alcançado.")

tv = TV()

while True:
    print("1. Mudar Canal")
    print("2. Aumentar Volume")
    print("3. Diminuir Volume")
    print("4. Desligar TV")

    opcao = input("Escolha a opção: ")

    if opcao == '1':
        novo_canal = int(input("Digite o número do novo canal: "))
        tv.mudar_canal(novo_canal)
    elif opcao == '2':
        tv.aumentar_volume()
    elif opcao == '3':
        tv.diminuir_volume()
    elif opcao == '4':
        print("Desligando a TV...")
        break
    else:
        print("Opção inválida. Tente novamente.")
