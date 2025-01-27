
class Celular:
    def __init__(self, marca, modelo, polegadas, armazenamento, memoria_ram):
        self.marca = marca
        self.modelo = modelo
        self.polegadas = polegadas
        self.armazenamento = armazenamento
        self.memoria_ram = memoria_ram
        self.status_celular = False
        self.status_chamada = False

    def ligar_celular(self):
        if self.status_celular == False:
            self.status_celular = True
            print('Celular ligado')
        else:
            print('Celular já está ligado')

    def desligar_celular(self):
        if self.status_celular == True:
            self.status_celular = False
            print('Celular desligado')
        else:
            print('Celular já está desligado')
    
    def fazer_chamada(self, numero):
        if self.status_celular == True:
            if self.status_chamada == False:
                self.status_chamada = True
                print('Chamada iniciada')
            else:
                print('Chamada já está em andamento')
        else:
            print('Celular está desligado')
    
    def encerrar_chamada(self):
        if self.status_celular == True:
            if self.status_chamada == True:
                self.status_chamada = False
                print('Chamada encerrada')
            else:
                print('Chamada já está encerrada')
        else:
            print('Celular está desligado')


    
    
