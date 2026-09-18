from .pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome=str, idade=int, curso=str, turma=str):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazerMatricula(self):
        print(f'Aluno(a) {self.nome} fez sua matrícula')

    def estudar(self):
        print(f'O(a) aluno(a) {self.nome}estuda {self.curso} na turma {self.turma}')