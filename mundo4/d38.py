"""
# Video com os desafios:  CeV Python POO: Aula 15 https://www.youtube.com/watch?v=PAGg0NgeMX4&list=PLHz_AreHm4dn_RXXoa3Ameh77f95Hgwv3&index=36

EXERCÍCIO D38 - Adicionar por agregação
Crie um programa que:
1. Contenha a classe Carrinho contendo:
    - _lista_produtos
    - _total - property
    - __str__(self) - retorna a lista de produtos e o total
2. Crie a classe Produto contendo:
    - _nome
    - _preco
3. Adicione produtos ao carrinho e calcule o total dos produtos adicionados automaticamente

Exemplo de uso:
carrinho = Carrinho()
produto1 = Produto("Produto 1", 10.0)
carrinho = carrinho + produto1
"""

class Carrinho():
    def __init__(self, lista_produtos:list = []):
        self._lista_produtos = lista_produtos


    @property
    def total(self):
        sumTotal = sum(p._preco for p in self._lista_produtos)
        return f'R$ {sumTotal:.2f}'

    def __str__(self):
        linha = '\n' + '-' * 30
        itens = '\n'.join(str(p) for p in self._lista_produtos)
        return f'{itens}{linha}\nTotal {self.total}'

    def __add__(self, other):
        if isinstance (other, Produto):
            return Carrinho(self._lista_produtos + [other])
        elif isinstance(other, Carrinho):
            return Carrinho(self._lista_produtos + other._lista_produtos)
        else:
            raise TypeError('Objeto inválido para adicionar ao carrinho')


class Produto():
    def __init__(self, nome:str, preco:float):
        self._nome = nome
        self._preco = preco

    def __str__(self):
        return f'{self._nome}: R$ {self._preco:.2f}'


p1 = Produto('Notebook Avell', 7900)
p2 = Produto('Teclado Logitech', 280)
p3 = Produto('Mouse Red Dragon', 179)

c1 = Carrinho()
c2 = Carrinho()

c1 += p1
c1 += p2
c1 += p3

c2 += c1
c2 += p3
print(c2)
