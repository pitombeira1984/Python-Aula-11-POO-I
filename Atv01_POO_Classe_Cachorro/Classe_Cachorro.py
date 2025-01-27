

class Cachorro():
    def __init__(self, nome, idade, raca):
        self.nome = nome
        self.idade = idade
        self.raca = raca

    def latir(self):
        if self.raca == "Vira-Lata":
            print(f'{self.nome} apenas late!')
        else:
            print(f'{self.nome} apenas morde')

    def andar(self):
        if self.idade <= 1:
            print(f'{self.nome} ainda não anda!')
        else:
            print(f'{self.nome} Anda e Corre!')

    def dormir(self):
        print(f'{self.nome} está dormindo!')