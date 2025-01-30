
class fatura():
    def __init__(self, numero, descricao, quantidade, preco, vt_fatura):
        self.numero = numero
        self.descricao = descricao
        self.quantidade = quantidade
        self.preco = preco
        self.vt_fatura = vt_fatura
    
    def gerar_fatura(self):
        self.vt_fatura = self.quantidade * self.preco
        return self.vt_fatura
    
