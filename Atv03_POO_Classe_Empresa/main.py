
from Classe_Empresa import Funcionario

while True:
    print("1 - Cadastrar Funcionário")
    print("2 - Remover Funcionário")
    print("3 - Listar Funcionários")
    print("4 - Sair")
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        nome = input("Digite o nome do Funcionário: ")
        cardo = input("Digite o Cargo do Funcionário: ")
        salario = float(input("Digite o Salário do Funcionário: "))
        funcionario = Funcionario(nome, cardo, salario)
        funcionario.AdicionarFuncionario()
    elif opcao == 2:
        nome = input("Digite o nome do Funcionário: ")
        funcionario = Funcionario(nome, "", 0)
        funcionario.RemoverFuncionario()
    elif opcao == 3:
        funcionario.ListarFuncionarios()
    elif opcao == 4:
        break
    else:
        print("Opção inválida. Tente novamente.")