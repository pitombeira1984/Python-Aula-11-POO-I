from Classe_Fatura import fatura

def main():
    gerar_fatura = fatura(1, 'Mouse', 2, 50.00, 0)
    print(gerar_fatura.gerar_fatura())

main()
    