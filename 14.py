class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def obterNome(self):
        return self.nome

    def obterSalario(self):
        return self.salario

    def aumentarSalario(self, porcentualDeAumento):
        aumento = self.salario * (porcentualDeAumento / 100)
        self.salario += aumento

harry = Funcionario("Harry", 25000)
print("Salário inicial de Harry:", harry.obterSalario())

harry.aumentarSalario(10)
print("Novo salário de Harry após aumento de 10%:", harry.obterSalario())
