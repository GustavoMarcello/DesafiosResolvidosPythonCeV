"""
# Video com os desafios:  CeV Python POO: Aula 15 https://www.youtube.com/watch?v=PAGg0NgeMX4&list=PLHz_AreHm4dn_RXXoa3Ameh77f95Hgwv3&index=36

EXERCÍCIO D34 - Bônus Salarial
Crie um programa que:
1. Contenha a classe abstrata Funcionario contendo:
    - _nome
    - __salario
        - Implemente get e set para o atributo __salario
        - Colocar validação no set para que o salário não possa ser alterado
    - calcular_bonus_salarial()
2. Crie as classes Gerente, Designer e Desenvolvedor que herdam de Funcionario
3. Implemente o método calcular_bonus_salarial() de acordo com a regra:
    - Gerente: 15% do salário
    - Designer: 8% do salário
    - Desenvolvedor: 10% do salário
4. Implemente um print com nome e salário ao criar o objeto.
"""
from abc import ABC

class Funcionario(ABC):
    def __init__(self, nome:str, salario:float, indice_bonus:float):
        self._nome = nome
        if salario < 0:
            raise ValueError(f'Salario não pode ser negativo')
        self.__salario = salario
        self.__indice_bonus = indice_bonus

        print(f'{self.__class__.__name__} {self._nome} com salário R$ {self.salario:.2f} e bonus de {self.calcular_bonus_salarial()}')


    @property
    def salario(self) -> float:
        return self.__salario

    @salario.setter
    def salario(self, valor):
        raise PermissionError(f'Salario não pode ser alterado')

    def calcular_bonus_salarial(self):
        bonus = self.salario * self.__indice_bonus
        return bonus


class Gerente(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario, 0.15)


class Designer(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario, 0.08)


class Desenvolvedor(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario, 0.1)


gerente = Gerente('Mauricio', 5000)
designer = Designer('Priscila', 5000)
desenvolvedor = Desenvolvedor('Pedro', 5000)