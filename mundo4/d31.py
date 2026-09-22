"""
# Video com os desafios:  CeV Python POO: Aula 09 https://www.youtube.com/watch?v=CTbdydT9nlQ&list=PLHz_AreHm4dn_RXXoa3Ameh77f95Hgwv3&index=27

EXERCÍCIO D31 - properties de retangulo
Crie um programa que:
1. Contenha a classe Retangulo contendo:
    - _base
    - _altura
    - _area
    - _perimetro
    - base: property getter / setter
    - altura: property getter / setter
    - area: property
    - perimetro: property
    - medidas()

Obs* valide as propriedades para que não sejam aceitos valores negativos ou zero.
"""

class Retangulo:
    def __init__(self, base, altura):
        self._base = base
        self._altura = altura
        self._area = self._base * self._altura
        self._perimetro = (self._base * 2) + (self._altura * 2)


    @property
    def area(self):
        return self._base * self._altura

    @property
    def perimetro(self):
        return (self._base * 2) + (self._altura * 2)
    
    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, novoValor):
        self._base = novoValor
        self._area = self._base * self._altura
        self._perimetro = (self._base * 2) + (self._altura * 2)
        return self._base
    
    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, novoValor):
        self._altura = novoValor
        self._area = self._base * self._altura
        self._perimetro = (self._base * 2) + (self._altura * 2)
        return self._altura

    def medidas(self):
        print(f'Base: {self._base}')
        print(f'Altura: {self._altura}')
        print(f'Área: {self._area}')
        print(f'Perímetro: {self._perimetro}')
    

retangulo1 = Retangulo(4, 8)
retangulo1 = Retangulo(9, 12)
retangulo1.medidas()
