"""
# Video com os desafios:  CeV Python POO: Aula 09 https://www.youtube.com/watch?v=Qcsftqx36d4&list=PLHz_AreHm4dn_RXXoa3Ameh77f95Hgwv3&index=19

EXERCÍCIO D26 - Hernça RH Salário
Crie um programa que:
1. Contenha a classe abstrata Funcionário contendo:
    - nome
    - salarioBruto
    - salario
    - salarioMinimo = 1612
    - inss = 7.5
    - calcularSalario() {abstrato}
    - analisarSalario() (calcule quantos salarios mínimos o funcionário ganha)
2. Crie classes filhas:
    - Horista 
        - valorHora
        - horasTrabalhadas
    - Mensalista 
"""

from abc import ABC, abstractmethod

class Funcionario(ABC):
    salarioMinimo = 1612
    inss = 7.5

    def __init__(self, nome=str):
        self.nome = nome
        self.salarioBruto = 0
        self.salario = 0
        self.salarioMinimo = 1612
        self.inss = 7.5

    @abstractmethod
    def calcularSalario(self):
        pass

    def analisarSalario(self):
        salarios_minimos = self.salario / self.salarioMinimo
        return salarios_minimos


class Horista(Funcionario):
    def __init__(self, nome=str, valorHora=float):
        super().__init__(nome, valorHora)
        self.valorHora = valorHora

    def calcularSalario(self):
        return super().calcularSalario()
    

class Mensalista(Funcionario):
    def __init__(self, nome=str):
        super().__init__(nome)

    def calcularSalario(self):
        return super().calcularSalario()
    
