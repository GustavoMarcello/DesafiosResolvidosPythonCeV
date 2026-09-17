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
        self.salarioMinimo = 1612
        self.inss = 0.075
        

    @abstractmethod
    def calcularSalario(self):
        pass

    def analisarSalario(self):
        salariosMinimos = self.salario / self.salarioMinimo
        print(f'Esse funcionário ganha {salariosMinimos:.3f} salarios mínimos')


class Horista(Funcionario):
    def __init__(self, nome=str, valorHora=float, horasTrabalhadas=float):
        super().__init__(nome)
        self.valorHora = valorHora
        self.horasTrabalhadas = horasTrabalhadas
        self.salarioBruto = self.valorHora * self.horasTrabalhadas

    def calcularSalario(self):
        self.salario = self.salarioBruto - (self.salarioBruto * self.inss)
        print(f'O salario de {self.nome} é de R$ {self.salario}')
    

class Mensalista(Funcionario):
    def __init__(self, nome=str, salarioBruto=float):
        super().__init__(nome)
        self.salarioBruto = salarioBruto


    def calcularSalario(self):
        self.salario = self.salarioBruto - (self.salarioBruto * self.inss)
        print(f'O salario de {self.nome} é de R$ {self.salario}')
    

funcionario1 = Horista('Pedro', 26, 220)
funcionario1.calcularSalario()
funcionario1.analisarSalario()

funcionario2 = Mensalista('Juliana', 9500)
funcionario2.calcularSalario()
funcionario2.analisarSalario()