from abc import ABC
from random import randint

class Personagem(ABC):
    def __init__(self, nome=str, vida=int, golpes=list):
        self._nome = nome
        self._vida = vida
        self.golpes = golpes
        self.__vidaMaxima = self._vida
        self.__fatorCuraPocao = 6

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

    def _verificaVida(self, inimigo):
        if self.vida <= 0:
            print(f'{self.nome} chegou a 0 de vida e não pode mais atacar antes de se curar')
            return False
        if inimigo.vida <= 0:
            print(f'{inimigo.nome} chegou a 0 de vida e não pode mais receber dano antes de se curar')
            return False
        return True

    def _receberDano(self, valor):
        self._vida -= valor
        return self._vida

    def escolherAtaque(self):
        print('Escolha o ataque:')
        for i, ataque in enumerate(self.golpes):
            print(f'  {i+1} - {ataque}')

    def usarPocao(self):
        if self._vida < (self.__vidaMaxima - self.__fatorCuraPocao):
            self._vida += self.__fatorCuraPocao
            print(f'{self._nome} usou poção e ficou com {self._vida} de vida')
            return  True

        if (self.__vidaMaxima - self.__fatorCuraPocao) <= self._vida < self.__vidaMaxima:
            self._vida = self.__vidaMaxima
            print(f'{self._nome} usou poção e ficou com vida cheia de {self._vida}')
            return True

        print(f'{self._nome} está com a vida cheia de {self.vida} e não pode usar poção')
        return True