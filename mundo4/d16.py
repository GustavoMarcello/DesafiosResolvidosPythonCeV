"""
# Video com os desafios:  CeV Python POO: Aula 05 https://www.youtube.com/watch?v=dKeazBVTNf8&list=PLHz_AreHm4dn_RXXoa3Ameh77f95Hgwv3&index=9
EXERCÍCIO D16 - Classe Funcionário
Crie um programa que:
1. Contenha a classe Funcionario contendo atributos:
    - nomeFuncionario
    - setor
    - cargo
2. Crie o método apresentacao() para o funcionário se apresentar
"""

class Funcionario:
    def __init__(self, nomeFuncionario=str, cargo=str, setor=str):
        self.nomeFuncionario = nomeFuncionario
        self.cargo = cargo
        self.setor = setor

    def apresentacao(self):
        print(f'Olá, me chamo {self.nomeFuncionario}, sou {self.cargo} do setor de {self.setor}')


funcionario = Funcionario('Gustavo', 'Developer', 'AI e Chatbots')
funcionario.apresentacao()