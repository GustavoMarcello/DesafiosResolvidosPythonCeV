from .pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, nome=str, idade=int, especialidade=str, nivel=str):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def darAula(self):
        print(f'Professor(a) {self.nome} está dando aula')

    def estudar(self):
        print(f'O(a) professor(a) {self.nome} estudou até o nivel {self.nivel}')