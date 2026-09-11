"""
EXERCÍCIO D17 - Classe Produto
Crie um programa que:
1. Contenha a classe Produto contendo atributos:
    - nomeProduto
    - precoProduto
2. Crie o método etiqueta() para o apresentar nome e preço do produto
"""

class Produto:
    def __init__(self, nomeProduto=str, precoProduto=float):
        self.nomeProduto = nomeProduto
        self.precoProduto = precoProduto

    def etiqueta(self):
        print(f'\nProduto: {self.nomeProduto}\nValor: R$ {self.precoProduto:.2f}')


produto1 = Produto('Pokebola Pikachu', 115)
produto1.etiqueta()

produto2 = Produto('Cubo mágico', 32)
produto2.etiqueta()