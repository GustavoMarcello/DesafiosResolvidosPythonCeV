"""
# Video com os desafios:  CeV Python POO: Aula 09 https://www.youtube.com/watch?v=Qcsftqx36d4&list=PLHz_AreHm4dn_RXXoa3Ameh77f95Hgwv3&index=19

EXERCÍCIO D27 - Hernça RPG
Crie um programa que:
1. Contenha a classe abstrata Personagem contendo:
    - nome
    - vida
    - golpes
    - atacar(alvo, forca)
    - receberDano(dano)
    - curar()
2. Crie classes filhas:
    - Guerreiro 
    - Mago
"""

from abc import ABC, abstractmethod
from random import randint

class Personagem(ABC):
    def __init__(self, nome=str, vida=int, golpes=list, equipamentos=list):
        self.nome = nome
        self.vida = vida
        self.golpes = golpes
        self.equipamentos = equipamentos

    def rolarD20(self):
        return randint(1, 20)

    def atacar(self):
        pass

    def receberDano(self):
        pass

    def usarPocao(self):
        pass


class Mago(Personagem):
    def __init__(self, nome=str, vida=int, golpes=list):
        super().__init__(nome, vida, golpes)

    def fireball(self):
        pass

    def magicMissles(self):
        pass


class Gerreiro(Personagem):
    def __init__(self, nome=str, vida=int, golpes=list):
        super().__init__(nome, vida, golpes)

    def ataqueDesarmado(self):
        pass

    def ataqueComArma(self):
        pass

    def arremecarArma(self):
        pass

    

    