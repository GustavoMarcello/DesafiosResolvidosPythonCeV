# Declaração da Classe
class Gafanhoto:

    # Metodo Construtor 
    def __init__(self, nome="<desconhecido>", idade=0): 
        # Atributos
        self.nome = nome
        self.idade = idade

    # Metodos de Instancia
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f'{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade'

    def __str__(self):
        return f'Atributos do objeto:\n  nome: {self.nome}\n  idade: {self.idade}'
    

g1 = Gafanhoto("Gustavo Marcello", 30)
g1.aniversario()
print(g1.mensagem())
print(g1)
print(g1.__dict__) # retorna os atributos com valores do objeto

# g2 = Gafanhoto()
# print(g2.mensagem())