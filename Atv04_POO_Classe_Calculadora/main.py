from Classe_Claculadora import Calculadora, Soma, Subtracao, Multiplicacao, Divisao

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
            soma = Soma()
            soma.resultado(num1, num2)
        elif opcao == 2:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            subtracao = Subtracao()
            subtracao.resultado(num1, num2)
        elif opcao == 3:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            multiplicacao = Multiplicacao()
            multiplicacao.resultado(num1, num2)
        elif opcao == 4:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            divisao = Divisao()
            divisao.resultado(num1, num2)
        elif opcao == 5:
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()