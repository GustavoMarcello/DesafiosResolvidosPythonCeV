from .pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome=str, idade=int, cargo=str, setor=str):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def baterPonto(self):
        print(f'Funcionário(a) {self.nome} acabou de bater ponto')

    def estudar(self):
        print(f'O(a) funcionario(a) {self.nome} estudou para {self.cargo}')