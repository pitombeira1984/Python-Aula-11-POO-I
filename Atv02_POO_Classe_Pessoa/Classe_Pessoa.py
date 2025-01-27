
class Pessoa():
    def __init__(self, nome, idade, peso, genero):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.genero = genero

    def FaixaEtaria(self):
        if self.idade <= 12:
            print(f'{self.nome} é criança!')
        elif self.idade > 12 and self.idade <= 18:
            print(f'{self.nome} é adolescente!')
        elif self.idade > 18 and self.idade <= 60:
            print(f'{self.nome} é adulto!')
        else:
            print(f'{self.nome} é idoso!')

    def FaixaPeso(self):
        if self.peso <= 50:
            print(f'{self.nome} está abaixo do peso!')
        elif self.peso > 50 and self.peso <= 70:
            print(f'{self.nome} está com o peso ideal!')
        else:
            print(f'{self.nome} está acima do peso!')

    def Genero(self):
        if self.genero == 'M':
            print(f'{self.nome} é do sexo masculino!')
        elif self.genero == 'F':
            print(f'{self.nome} é do sexo feminino!')
        else:
            print(f'{self.nome} não informou o sexo!')