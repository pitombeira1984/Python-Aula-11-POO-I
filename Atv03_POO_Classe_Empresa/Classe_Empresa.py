
funcionarios = []

class Funcionario():
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo  
        self.salario = salario
        
    def AdicionarFuncionario(self):
        funcionarios.append(self)
        print(f'{self.nome} foi adicionado(a) com sucesso!')
        
    def ListarFuncionarios(self):
        for funcionario in funcionarios:
            if funcionario.nome == self.nome:
                print(f'Nome: {self.nome} | Cargo: {self.cargo} | Salário: {self.salario}')
                return
        print(f'{self.nome} não foi encontrado(a) na lista de funcionários.')
            
    def RemoverFuncionario(self):
        for funcionario in funcionarios:
            if funcionario.nome == self.nome:
                funcionarios.remove(funcionario)
                print(f'{self.nome} foi removido(a) com sucesso!')
                return
        print(f'{self.nome} não foi encontrado(a) na lista de funcionários.')