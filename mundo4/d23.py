"""
# Video com os desafios:  CeV Python POO: Aula 09 https://www.youtube.com/watch?v=Qcsftqx36d4&list=PLHz_AreHm4dn_RXXoa3Ameh77f95Hgwv3&index=19

EXERCÍCIO D23 - Hernça polígono
Crie um programa que:
1. Contenha a classe abstrata Polígono contendo:
    - qtdLados
    - perímetro()
    - area()
2. Crie classes filhas:
    - quadrado - atributo tamanhoLado
    - circulo - atributo raio
"""
from abc import ABC, abstractmethod
from math import pi

class Poligono(ABC):
    def __init__(self, qtdLados=int):
        super().__init__()
        self.qtdLados = qtdLados

    @abstractmethod
    def perimetro(self) -> float:
        pass

    @abstractmethod
    def area(self) -> float:
        pass

class Quadrado(Poligono):
    def __init__(self, tamanhoLado=float):
        super().__init__(4)
        self.tamanhoLado = tamanhoLado

    def perimetro(self):
        return self.tamanhoLado * self.qtdLados

    def area(self):
        return self.tamanhoLado * self.tamanhoLado
    

class Circulo(Poligono):
    def __init__(self, raio=float):
        super().__init__(0)
        self.raio = raio

    def perimetro(self):
        return 2 * pi * self.raio

    def area(self):
        return pi * self.raio ** 2


quadrado = Quadrado(5)
circulo = Circulo(3)

print(quadrado.__dict__)
print(f'O quadrado de lado {quadrado.tamanhoLado} cm, tem área de {quadrado.area():.2f} cm²')
print(f'O quadrado de lado {quadrado.tamanhoLado} cm, tem perímetro de {quadrado.perimetro():.2f} cm')
print(circulo.__dict__)
print(f'O circulo de raio {circulo.raio} cm, tem área de {circulo.area():.2f} cm²')
print(f'O circulo de raio {circulo.raio} cm, tem perímetro de {circulo.perimetro():.2f} cm')