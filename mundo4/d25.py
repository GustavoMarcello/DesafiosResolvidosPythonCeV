"""
# Video com os desafios:  CeV Python POO: Aula 09 https://www.youtube.com/watch?v=Qcsftqx36d4&list=PLHz_AreHm4dn_RXXoa3Ameh77f95Hgwv3&index=19

EXERCÍCIO D25 - Hernça Transportadora
Crie um programa que:
1. Contenha a classe abstrata Transporte contendo:
    - distância
    - valorFrete
    - calcFrete()
2. Crie classes filhas:
    - Moto 
        - fator = 0.5
        - distancia livre
    - Caminhão 
        - fator = 1.2
        - distancia mínima 50 km
    - Drone 
        - fator = 9.5
        - distancia máxima 10 km
"""
from abc import ABC, abstractmethod

class Transporte(ABC):
    def __init__(self, distancia=float):
        self.distancia = distancia
        self.valorFrete = 0

    @abstractmethod
    def calcularFrete(self):
        pass


class Moto(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia)
        self.fator = 0.5

    def calcularFrete(self):
        self.valorFrete = self.distancia * self.fator
        print(f'Valor do frete de Moto: R$ {self.valorFrete}')

    
class Caminhao(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia)
        self.fator = 1.2

    def calcularFrete(self):
        if self.distancia < 50:
            print('Distância menor que a mínima')
        else:
            self.valorFrete = self.distancia * self.fator
            print(f'Valor do frete de Caminhão: R$ {self.valorFrete}')


class Drone(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia)
        self.fator = 9.5

    def calcularFrete(self):
        if self.distancia > 10:
            print('Distância maior que a máxima')
        else:
            self.valorFrete = self.distancia * self.fator
            print(f'Valor do frete de Drone: R$ {self.valorFrete}')


moto = Moto(20)
moto.calcularFrete()

caminhao = Caminhao(60)
caminhao.calcularFrete()

drone = Drone(8)
drone.calcularFrete()
