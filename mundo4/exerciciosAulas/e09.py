from abc import ABC

class Avaliacao(ABC):
    def __init__(self, nome=str, disciplina=str, nota=float):
        self.nome = nome
        self.disciplina = disciplina
        self._nota = nota
        print(f'Aluno(a) {self.nome} recebeu nota {self._nota} em {self.disciplina}')

    # atributo validável
    @property
    def nota(self):
        return self._nota

    @nota.setter
    def nota(self, novaNota):
        if 0 <= novaNota <= 10:
            self._nota = novaNota
        else:
            print('Nova nota inválida')


avaliacao1 = Avaliacao('Gustavo Marcello', 'Programação', 8.3)
