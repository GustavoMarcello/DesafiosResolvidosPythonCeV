"""
# Video com os desafios:  CeV Python POO: Aula 15 https://www.youtube.com/watch?v=PAGg0NgeMX4&list=PLHz_AreHm4dn_RXXoa3Ameh77f95Hgwv3&index=36

EXERCÍCIO D37 - Sistema de mensagens
Crie um programa que:
1. Contenha a classe Mensagem contendo:
    - __texto
    - __tipo
    - __cor
    - mostrar()
2. Crie as classes Erro e Alerta que herdam de Mensagem
3. Implemente o método mostrar() de acordo com a regra:
    - Mensagem: "Mensagem: {texto} - Ícone: {icone}"
    - Erro em vermelho: "Erro: {texto} - Ícone: {icone}"
    - Alerta em amarelo: "Alerta: {texto} - Ícone: {icone}"
"""

class Mensagem():
    def __init__(self, texto:str, tipo:str = 'Aviso', cor:str = '30'):
        self.__texto = texto
        self.__tipo = tipo
        self.__cor = cor

    def mostrar(self):
        print(f'\033[{self.__cor}m{self.__tipo}: {self.__texto}\033m')


class Erro(Mensagem):
    def __init__(self, texto):
        super().__init__(texto, 'Erro', '31')


class Alerta(Mensagem):
    def __init__(self, texto):
        super().__init__(texto, 'Alerta', '33')


m1 = Mensagem('Esta é uma mensagem')
m2 = Erro('Este é um erro')
m3 = Alerta('Este é um alerta')

m1.mostrar()
m2.mostrar()
m3.mostrar()