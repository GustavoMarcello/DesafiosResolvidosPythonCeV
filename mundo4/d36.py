"""
# Video com os desafios:  CeV Python POO: Aula 15 https://www.youtube.com/watch?v=PAGg0NgeMX4&list=PLHz_AreHm4dn_RXXoa3Ameh77f95Hgwv3&index=36

EXERCÍCIO D36 - Simulador de diferentes tipos de pagamentos
Crie um programa que:
1. Contenha a classe abstrata Pagamento contendo:
    - __valor
    - @fvalor: property retornando valor formatado em R$ 0,00
    - pagar() - "Pagando valor de {fvalor} via {__class__.__name__}"
2. Crie as classes Boleto, Credito e Pix que herdam de Pagamento
"""
from abc import ABC

class Pagamento(ABC):
    def __init__(self, valor:float):
        self.__valor = valor

    
    @property
    def fvalor(self) -> str:
        return f'R$ {self.__valor:.2f}'

    def pagar(self):
        print(f'Pagando valor de {self.fvalor} via {self.__class__.__name__}')


class Boleto(Pagamento):
    def __init__(self, valor):
        super().__init__(valor)


class Pix(Pagamento):
    def __init__(self, valor):
        super().__init__(valor)


class Credito(Pagamento):
    def __init__(self, valor):
        super().__init__(valor)


conta1 = Boleto(1500)
conta2 = Pix(300)
conta3 = Credito(4200)

conta1.pagar()
conta2.pagar()
conta3.pagar()
