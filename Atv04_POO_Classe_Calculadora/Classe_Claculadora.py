
class Calculadora:
    def resultado(self):
        print(f'O resultado da operação é: ')
        
class Soma(Calculadora):
    def resultado(self, num1, num2):
        super().resultado()
        print(num1 + num2)

class Subtracao(Calculadora):
    def resultado(self, num1, num2):
        super().resultado()
        print(num1 - num2)

class Multiplicacao(Calculadora):
    def resultado(self, num1, num2):
        super().resultado()
        print(num1 * num2)

class Divisao(Calculadora):
    def resultado(self, num1, num2):
        super().resultado()
        print(num1 / num2)        
        