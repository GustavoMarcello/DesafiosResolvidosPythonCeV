from functools import singledispatchmethod

class Analisador():
    def __init__(self):
        pass

    @singledispatchmethod
    def analisar(self, valor):
        print(f'Não foi possível anaisar {valor}')

    @analisar.register
    def _(self, valor:int):
        print(f'{valor} é do tipo int')

    @analisar.register
    def _(self, valor:str):
        print(f"'{valor}' é do tipo str")

    @analisar.register
    def _(self, valor: tuple|list|dict):
        print(f'{valor} é uma coleção de dados')


analisador = Analisador()
analisador.analisar(3)
analisador.analisar(3.8)
analisador.analisar('Python')
analisador.analisar(None)