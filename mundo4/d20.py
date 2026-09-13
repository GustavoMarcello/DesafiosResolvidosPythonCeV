"""
# Video com os desafios:  CeV Python POO: Aula 05 https://www.youtube.com/watch?v=dKeazBVTNf8&list=PLHz_AreHm4dn_RXXoa3Ameh77f95Hgwv3&index=9

EXERCÍCIO D20 - Classe Gamer
Crie um programa que:
1. Contenha a classe Gamer contendo atributos:
    - nomeUsuario
    - nickGamer
    - jogosFavoritos
2. Crie os métodos:
    - addFavorito() para adicionar um jogo na lista de favoritos
    - fichaGamer() que demonstra todos os atributos com jogos em ordem alfabética
"""

class Gamer:
    def __init__(self, nomeUsuario=str, nickGamer=str, jogosFavoritos=list):
        self.nomeUsuario = nomeUsuario
        self.nickGamer = nickGamer
        self.jogosFavoritos = jogosFavoritos

    def fichaGamer(self):
        print(f'\nNome: {self.nomeUsuario} Nick: {self.nickGamer}')
        print(f'Jogos favoritos')
        for i, j in enumerate(self.jogosFavoritos):
            print(f'{i+1} - {j}')

    def addFavorito(self, nomeFavorito=str):
        self.jogosFavoritos.append(nomeFavorito)
        print('Jogo adicionado com sucesso')
        

gustavo = Gamer('Gustavo', 'gugamarcello', ['Overwatch', 'Dont Starve', 'Elden Ring', 'Cuphead'])
gustavo.fichaGamer()
gustavo.addFavorito('The Witcher')
gustavo.fichaGamer()
