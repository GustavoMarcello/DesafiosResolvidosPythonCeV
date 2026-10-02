"""
# Video com os desafios:  CeV Python POO: Aula 15 https://www.youtube.com/watch?v=PAGg0NgeMX4&list=PLHz_AreHm4dn_RXXoa3Ameh77f95Hgwv3&index=36

EXERCÍCIO D35 - Simulador de abertura de arquivos
Crie um programa que:
1. Contenha a classe abstrata Arquivo contendo:
    - _nome
    - _extensao
    - _tamanho (em Megas)
    - @nomecompleto: property retornando 'nome + extensao + tamanho'
    - abrir() - abstractmethod
2. Crie as classes PDF e DOC que herdam de Arquivo
3. Implemente o método abrir() de acordo com a regra:
    - PDF: "Abrindo arquivo PDF de tamanho {tamanho} Mb no Navegador"
    - DOC: "Abrindo arquivo DOC de tamanho {tamanho} Mb no Word"
"""
from abc import ABC, abstractmethod

class Arquivo(ABC):
    def __init__(self, nome:str, extensao:str, tamanho_megas:float):
        self._nome = nome
        self._tamanho = tamanho_megas
        self._extensao = extensao

        print(self.nome_completo)

    @property
    def nome_completo(self):
        return f"'{self._nome}{self._extensao}' ({self._tamanho:.2f} MB)"

    @abstractmethod
    def abrir(self):
        pass


class PDF(Arquivo):
    def __init__(self, nome, tamanho):
        super().__init__(nome, '.pdf', tamanho)

    def abrir(self):
        print(f'Abrindo {self.nome_completo} no Navegador')


class DOC(Arquivo):
    def __init__(self, nome, tamanho):
        super().__init__(nome, '.doc', tamanho)


    def abrir(self):
        print(f'Abrindo {self.nome_completo} no Word')


a1 = PDF('boleto', 250)
a2 = DOC('contrato', 1300)

a1.abrir()
a2.abrir()