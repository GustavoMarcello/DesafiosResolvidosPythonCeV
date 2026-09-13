"""
# Video com os desafios:  CeV Python POO: Aula 05 https://www.youtube.com/watch?v=dKeazBVTNf8&list=PLHz_AreHm4dn_RXXoa3Ameh77f95Hgwv3&index=9
EXERCÍCIO D18 - Classe Churrasco
Crie um programa que:
1. Contenha a classe Churrasco contendo parâmetro:
    - qtdPessoas
2. Crie o método para calcular:
    - Quantos Kg de carne devem ser comprados
    - O valor total a ser gasto
    - O valor por pessoa
3. Considere:
    - Consumo padrão: 400g de carne por pessoa
    - Preço médio das carnes: R$ 82,40 / Kg
"""

class Churrasco:
    def __init__(self, qtdPessoas=int):
        self.qtdPessoas = qtdPessoas
        self.consumoPadrao = 0.4
        self.precoMedio = 82.4
        self.qtdTotalKgCarne = 0.0
        self.precoTotal = 0.0
        self.precoPorPessoa = 0.0

    def calculo(self):
        qtdTotalKgCarne = self.qtdPessoas * self.consumoPadrao
        precoTotal = qtdTotalKgCarne * self.precoMedio

        self.qtdTotalKgCarne = qtdTotalKgCarne
        self.precoTotal = precoTotal
        self.precoPorPessoa = precoTotal / self.qtdPessoas
        
        print(f'\nCondições do Churras: \nTotal pessoas: {self.qtdPessoas}\nQuantidade total de carne: {self.qtdTotalKgCarne:.2f} Kg\nPreço total: R$ {self.precoTotal:.2f}\nPreço por pessoa: R$ {self.precoPorPessoa:.2f}')


churras= Churrasco(12)
churras.calculo()