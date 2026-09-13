"""
# Video com os desafios:  CeV Python POO: Aula 09 https://www.youtube.com/watch?v=Qcsftqx36d4&list=PLHz_AreHm4dn_RXXoa3Ameh77f95Hgwv3&index=19

EXERCÍCIO D24 - Hernça cafeteria
Crie um programa que:
1. Contenha a classe abstrata Bebidas contendo:
    - tamanho [P, M, G]
    - quente [True, False]
    - preparar() abstrato
    - ferverAgua() abstrato
    - adicionarGelo() abstrato
    - misturar() abstrato
    - servir() abstrato
2. Crie classes filhas:
    - Cafe
    - Cha
    - Capuchino
"""
from abc import ABC, abstractmethod
from time import sleep

class Bebidas(ABC):
    def __init__(self, tamanho=str, quente=bool):
        self.tamanho = tamanho
        self.quente = quente
        self.temperatura = 'frio'

    def ferverAgua(self):
        print('Fervendo a água')
        sleep(1)

    def adicionarGelo(self):
        print('Adicionando gelo')
        sleep(1)

    def misturar(self):
        print('Misturando')
        sleep(1)

    @abstractmethod
    def preparar(self):
        pass


class Cafe(Bebidas):
    def __init__(self, tamanho=str, quente=bool):
        super().__init__(tamanho, quente)

        if self.quente:
            self.temperatura = 'quente'

        print(f'Seu café {self.temperatura} {self.tamanho} será preparado')

    def preparar(self):
        if self.quente:
            self.ferverAgua()
        else:
            self.adicionarGelo()
        self.misturar()
        print(f'Seu café {self.temperatura} {self.tamanho} está pronto\n')


class Cha(Bebidas):
    def __init__(self, tamanho=str, quente=bool):
        super().__init__(tamanho, quente)

        if self.quente:
            self.temperatura = 'quente'

        print(f'Seu chá {self.temperatura} {self.tamanho} será preparado')

    def preparar(self):
        if self.quente:
            self.ferverAgua()
        else:
            self.adicionarGelo()
        self.misturar()
        print(f'Seu chá {self.temperatura} {self.tamanho} está pronto\n')


class Capuchino(Bebidas):
    def __init__(self, tamanho=str, quente=bool):
        super().__init__(tamanho, quente)

        if self.quente:
            self.temperatura = 'quente'

        print(f'Seu capuchino {self.temperatura} {self.tamanho} será preparado')

    def preparar(self):
        if self.quente:
            self.ferverAgua()
        else:
            self.adicionarGelo()
        self.misturar()
        print(f'Seu capuchino {self.temperatura} {self.tamanho} está pronto\n')


cafe = Cafe('pequeno', False)
cha = Cha('medio', True)
capuchino = Capuchino('grande', False)

cafe.preparar()
cha.preparar()
capuchino.preparar()
