class Calculadora:
    def __init__(self):
        self.n1 = float(input("Digite o Nº1: "))
        self.n2 = float(input("Digite o Nº2: "))
        self.opcao = input("Escolha a operação: ")

    def operacao(self):
        if self.opcao == "1":
            return self.n1 + self.n2
        if self.opcao == "2":
            return self.n1 - self.n2
        if self.opcao == "3":
            return self.n1 * self.n2
        if self.opcao == "4":
            return self.n1 / self.n2