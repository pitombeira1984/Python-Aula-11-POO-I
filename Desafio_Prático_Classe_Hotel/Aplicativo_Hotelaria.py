
class Hotel:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []
        self.quartos = []
        self.reservas = []

    def contratar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def adicionar_quarto(self, quarto):
        self.quartos.append(quarto)

    def reservar_quarto(self, cliente, quarto, data_inicio, data_fim):
        if quarto.disponivel:
            reserva = Reserva(cliente, quarto, data_inicio, data_fim)
            self.reservas.append(reserva)
            quarto.disponivel = False
            return reserva
        else:
            return "Quarto indisponível"

    def calcular_conta(self, reserva):
        diaria = reserva.quarto.diaria
        num_diarias = (reserva.data_fim - reserva.data_inicio).days
        return diaria * num_diarias

class Funcionario:
    def __init__(self, nome, funcao, salario):
        self.nome = nome
        self.funcao = funcao
        self.salario = salario

class Quarto:
    def __init__(self, numero, tipo, diaria):
        self.numero = numero
        self.tipo = tipo
        self.diaria = diaria
        self.disponivel = True

class Reserva:
    def __init__(self, cliente, quarto, data_inicio, data_fim):
        self.cliente = cliente
        self.quarto = quarto
        self.data_inicio = data_inicio
        self.data_fim = data_fim

# Exemplos de uso
hotel = Hotel("Hotel Exemplo")

funcionario1 = Funcionario("João", "Recepcionista", 2000)
hotel.contratar_funcionario(funcionario1)

quarto1 = Quarto(101, "Suíte", 300)
hotel.adicionar_quarto(quarto1)

# Para utilizar datas, você pode usar o módulo datetime:
from datetime import date

cliente1 = "Hóspede Exemplo"
data_inicio = date(2024, 5, 1)
data_fim = date(2024, 5, 5)

reserva1 = hotel.reservar_quarto(cliente1, quarto1, data_inicio, data_fim)

if isinstance(reserva1, Reserva):
    print("Reserva realizada com sucesso!")
    conta = hotel.calcular_conta(reserva1)
    print("Valor da conta:", conta)
else:
    print(reserva1) 