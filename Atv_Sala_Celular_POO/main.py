from Class_Celular import Celular

aparelho_celular = Celular("Samsung", "GAlaxy S23", 3.12, 120, 8)

while True:
    print("1 - Ligar celular")
    print("2 - Desligar Celular")
    print("3 - Fazer Chamada")
    print("4 - Encerrar Chamada")
    print("5 - Sair")
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        aparelho_celular.ligar_celular()

    elif opcao == 2:
        aparelho_celular.desligar_celular()

    elif opcao == 3:
        numero = input("Digite o número para fazer a chamada: ")
        aparelho_celular.fazer_chamada(numero)
        print(f"Chamando para o número {numero}")

    elif opcao == 4:
        aparelho_celular.encerrar_chamada()

    elif opcao == 5:
        print("Saindo...")
        
    