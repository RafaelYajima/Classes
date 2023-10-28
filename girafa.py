
class Girafa:
    # Propriedades


    # O metodo __init__ é executado quando a classe é instanciada
    def __init__(self, nome, altura, cor, idade, origem):
        self.nome = nome
        self.altura = altura
        self.cor = cor
        self.idade = idade
        self.origem = origem
        self.__fome = 100

    def andar(self):
        print(self.nome, "está andando...")

    def comer(self, alimento):
        lista_alimentos = ['folhas', 'frutas', 'plantas']
        
        if alimento in lista_alimentos:
            self.__fome -= 10
        else:
            print(self.nome, "não come esse tipo de coisa...")

    def fome(self):
        if self.__fome > 60:
            print(self.nome, "está morrendo de fome")
        elif self.__fome > 40:
            print(self.nome, "está com fome")
        elif self.__fome > 20:
            print(self.nome, "está saciada")
        elif self.__fome > 10:
            print(self.nome, "está cheia")
        elif self.__fome < 0:
            print(self.nome, "está explodindo")

    def andar(self):
        print()

    def respira(self):
        print()

    def reproduz(self):
        print()