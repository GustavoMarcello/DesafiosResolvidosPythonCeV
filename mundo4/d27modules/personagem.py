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
        print(f'Resultado D12: {resultado}')
        return resultado

    def rolarD6(self):
        resultado = randint(1, 6)
        print(f'Resultado D6: {resultado}')
        return resultado

    def atacar(self):
        print('Escolha o ataque:\n')
        for i, ataque in enumerate(self.golpes):
            print(f'{i} - {ataque}\n')

    def receberDano(self, valor):
        self._vida -= valor
        return self._vida

    def usarPocao(self):
        self._vida += 6
        return self._vida