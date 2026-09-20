from abc import ABC, abstractmethod
from random import randint

class Personagem(ABC):
    def __init__(self, nome=str, vida=int, golpes=list):
        self._nome = nome
        self._vida = vida
        self.golpes = golpes

    @property
    def nome(self):
        return self._nome

    @property
    def vida(self):
        return self._vida


    def rolarD12(self):
        resultado = randint(1, 12)
        return resultado

    def rolarD6(self):
        resultado = randint(1, 6)
        return resultado

    def escolherAtaque(self):
        print('Escolha o ataque:')
        for i, ataque in enumerate(self.golpes):
            print(f'  {i+1} - {ataque}')

    def receberDano(self, valor):
        self._vida -= valor
        return self._vida

    def usarPocao(self):
        self._vida += 6
        return self._vida