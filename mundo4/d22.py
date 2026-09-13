"""
# Video com os desafios:  CeV Python POO: Aula 05 https://www.youtube.com/watch?v=dKeazBVTNf8&list=PLHz_AreHm4dn_RXXoa3Ameh77f95Hgwv3&index=9

EXERCÍCIO D22 - Classe ControleRemoto
Crie um programa que:
1. Contenha a classe ControleRemoto contendo entre os demais atributos:
    - canalAtual
    - volumeTotal
    - tvLigada
2. Crie o métodos para:
    - Ligar e desligar a TV
    - Aumentar e reduzir o volume (volume máximo = 20)
    - Subir e descer de canais
    - Ir para canal desejado
"""

class ControleRemoto:
    def __init__(self):
        self.canalAtual = 1
        self.canalMinimo = 1
        self.canalMaximo = 8
        self.volumeMinimo = 0 
        self.volumeMaximo = 20 
        self.volumeAtual = 10
        self.tvLigada = False


    def __str__(self):
        if not self.tvLigada:
            return f'Status da TV: DESLIGADA'
        return f'Status da TV: Canal {self.canalAtual} Volume {self.volumeAtual}'

    def msgDesligada(self):
        print('Impossível ações com TV desligada')

    def ligarTv(self):
        if self.tvLigada:
            print(f'TV já está ligada, canal {self.canalAtual} volume {self.volumeAtual}')
        else:
            self.tvLigada = True
            print(f'TV foi ligada, canal {self.canalAtual} volume {self.volumeAtual}')

    def desligarTv(self):
        if not self.tvLigada:
            print(f'TV já está desligada')
        else:
            self.tvLigada = False
            print(f'TV foi desligada')
        
    def avancarCanal(self):
        if not self.tvLigada:
            self.msgDesligada()
            return
        
        self.canalAtual += 1

        if self.canalAtual > self.canalMaximo:
            self.canalAtual = self.canalMinimo

        print(f'Canal atual: {self.canalAtual}')
        
    def reduzirCanal(self):
        if not self.tvLigada:
            self.msgDesligada()
            return
        
        self.canalAtual -= 1

        if self.canalAtual < self.canalMinimo:
            self.canalAtual = self.canalMaximo

        print(f'Canal atual: {self.canalAtual}')
        
    def aumentarVolume(self):
        if not self.tvLigada:
            self.msgDesligada()
            return
        
        self.volumeAtual += 1

        if self.volumeAtual > self.volumeMaximo:
            self.volumeAtual = self.volumeMaximo
            print(f'Volume atual: {self.volumeAtual}, já está no máximo')
        else:
            print(f'Volume atual: {self.volumeAtual}')
        
    def reduzirVolume(self):
        if not self.tvLigada:
            self.msgDesligada()
            return
        
        self.volumeAtual -= 1

        if self.volumeAtual < self.volumeMinimo:
            self.volumeAtual = self.volumeMinimo
            print(f'Volume atual: {self.volumeAtual}, já está no mínimo')
        else:
            print(f'Volume atual: {self.volumeAtual}')


    
controleRemoto = ControleRemoto()
print(controleRemoto)
controleRemoto.ligarTv()
controleRemoto.aumentarVolume()
controleRemoto.reduzirVolume()
controleRemoto.avancarCanal()
controleRemoto.reduzirCanal()
controleRemoto.desligarTv()
