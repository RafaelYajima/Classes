class Calculadora:
    
    def __init__(self):
        self.n1 = 0
        self.n2 = 0

    def somar(self):
        self.verifica_numeros()
        return self.n1 + self.n2

    def multiplicar(self):
        self.verifica_numeros()
        return self.n1 * self.n2

    def dividir(self):
        self.verifica_numeros()

        if self.n2 == 0:
            print("Não é possivel dividir por zero")
            return
        return self.n1 / self.n2

    def elevar(self):
        self.verifica_numeros()
    
        return self.n1 ** self.n2
    
    def subtractir(self):
        self.verifica_numeros()
        return self.n1 - self.n2
    
    def verifica_numeros(self):
        if not isinstance(self.n1, (int, float)):
            print("O numero um não é valido")

        if not isinstance(self.n2, (int, float)):
            print("O numero dois não é valido")

    def solicita_numeros(self):
        self.n1 = float(input("Digite o primeiro numero: "))
        self.n2 = float(input("Digite o segundo numero: "))