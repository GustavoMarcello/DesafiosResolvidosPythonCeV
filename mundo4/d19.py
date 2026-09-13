"""
# Video com os desafios:  CeV Python POO: Aula 05 https://www.youtube.com/watch?v=dKeazBVTNf8&list=PLHz_AreHm4dn_RXXoa3Ameh77f95Hgwv3&index=9

EXERCÍCIO D19 - Classe Livro
Crie um programa que:
1. Contenha a classe Livro contendo atributos:
    - nomeLivro
    - totalPaginas = 50
    - paginaAtual
2. Crie os métodos:
    - avancarPag() para avançar uma quantidade de paginas informado pelo usuário
    - retornarPag() para avançar uma quantidade de paginas informado pelo usuário
3. O Programa deverá:
    - informar em qual pagina o usuário está.
    - informar que o usuário chegou ao fim
    - O usuário poderá cessar apenas entre a primeira e última página
"""

class Livro:
    def __init__(self, nomeLivro=str):
        self.nomeLivro = nomeLivro.upper()
        self.totalPaginas = 50 
        self.paginaAtual = 1

        print(f'Este é o livro {self.nomeLivro}, ele contém {self.totalPaginas} páginas')

    def avancarPag(self, qtdPaginas):
        self.paginaAtual += qtdPaginas

        if self.paginaAtual > self.totalPaginas:
            self.paginaAtual = self.totalPaginas
            print(f'\nLivro {self.nomeLivro}\nVocê chegou na última página: {self.paginaAtual}')
        else:
            print(f'\nLivro {self.nomeLivro}\nVocê está na pág: {self.paginaAtual}')

    def retornarPag(self, qtdPaginas):
        self.paginaAtual -= qtdPaginas

        if self.paginaAtual < 1:
            self.paginaAtual = 1
            print(f'\nLivro {self.nomeLivro}\nVocê chegou na primeira página: {self.paginaAtual}')
        else:
            print(f'\nLivro {self.nomeLivro}\nVocê está na pág: {self.paginaAtual}')

livro1 = Livro('Aprendendo Python')
livro1.avancarPag(15)
livro1.avancarPag(45)
livro1.retornarPag(4)
livro1.retornarPag(64)