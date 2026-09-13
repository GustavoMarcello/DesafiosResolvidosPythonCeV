from abc import ABC, abstractmethod

class Pessoa(ABC): #Abstract Base Classes
    def __init__(self, nome=str, idade=int):
        self.nome = nome
        self.idade = idade

    def aniversario(self):
        self.idade += 1

    @abstractmethod
    def estudar():
        pass