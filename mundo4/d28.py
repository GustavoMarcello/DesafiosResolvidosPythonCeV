"""
# Video com os desafios:  CeV Python POO: Aula 12 https://www.youtube.com/watch?v=CTbdydT9nlQ&list=PLHz_AreHm4dn_RXXoa3Ameh77f95Hgwv3&index=27

EXERCÍCIO D28 - Termostato
Crie um programa que:
1. Contenha a classe abstrata Termostato contendo:
    - temperatura mínima 18 graus
    - temperatura máxima 30 graus
    - temperatura inicial 24 graus
    - temperatura atual = __temperatura
    - aumentar() de 0.5 em 0.5 graus
    - diminuir() de 0.5 em 0.5 graus
2. Crie as propriedade:
    - temperatura: get
"""

class Termostato:
    def __init__(self):
        self._tempMin = 18
        self._tempMax = 30
        self._tempAtual = 24


    @property
    def tempMin(self):
        return self._tempMin
    
    @property
    def tempMax(self):
        return self._tempMax
    
    @property
    def tempAtual(self):
        return self._tempAtual
    

    def aumentar(self):
        if self._tempAtual == self._tempMax:
            print(f'Limite máximo {self._tempAtual} °C')
        else:
            self._tempAtual += 0.5
            print(f'Aumentou temperatura para {self._tempAtual} °C')

    def diminuir(self):
        if self._tempAtual == self._tempMin:
            print(f'Limite mínimo {self._tempAtual} °C')
        else:
            self._tempAtual -= 0.5
            print(f'Diminuiu temperatura para {self._tempAtual} °C')

termo = Termostato()
print(termo.tempAtual)
termo.diminuir()
termo.aumentar()