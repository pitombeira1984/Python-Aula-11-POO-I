from Classe_Calculadora_1 import Calculator

def main():
    while True:
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Sair")
        opcao = int(input("Digite a opção desejada: "))
        if opcao == 1:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            calculadora = Calculator(num1, num2)
            print(f'O resultado da operação é: {calculadora.add()}')
        elif opcao == 2:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            calculadora = Calculator(num1, num2)
            print(f'O resultado da operação é: {calculadora.sub()}')
        elif opcao == 3:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            calculadora = Calculator(num1, num2)
            print(f'O resultado da operação é: {calculadora.mul()}')
        elif opcao == 4:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            calculadora = Calculator(num1, num2)
            print(f'O resultado da operação é: {calculadora.div()}')
        elif opcao == 5:
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()