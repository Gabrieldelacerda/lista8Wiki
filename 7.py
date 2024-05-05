class BichinhoVirtual:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alterarNome(self, novo_nome):
        self.nome = novo_nome

    def alterarFome(self, nova_fome):
        self.fome = nova_fome

    def alterarSaude(self, nova_saude):
        self.saude = nova_saude

    def alterarIdade(self, nova_idade):
        self.idade = nova_idade

    def retornarNome(self):
        return self.nome

    def retornarFome(self):
        return self.fome

    def retornarSaude(self):
        return self.saude

    def retornarIdade(self):
        return self.idade

    def retornarHumor(self):
        humor = (self.fome + self.saude) / 2
        if humor < 30:
            return "Triste"
        elif humor < 70:
            return "Normal"
        else:
            return "Feliz"

meu_bichinho = BichinhoVirtual(nome="Gaya", fome=50, saude=80, idade=2)

print("Nome:", meu_bichinho.retornarNome())
print("Fome:", meu_bichinho.retornarFome())
print("Saúde:", meu_bichinho.retornarSaude())
print("Idade:", meu_bichinho.retornarIdade())
print("Humor:", meu_bichinho.retornarHumor())

meu_bichinho.alterarFome(10)
print("Humor após alterar fome:", meu_bichinho.retornarHumor())
