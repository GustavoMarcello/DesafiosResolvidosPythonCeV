"""
EXERCÍCIO D107 - Módulos em Python
Crie um programa que:
1. Consuma o módulo moeda.py criado por você
2. Esse módulo contém as funções:
    - aumentar()
    - diminuir()
    - dobro()
    - metade()
3. Faça um programa que importe esse módulo e use essas funções
"""

import moeda

valor = 12

preco = float(input('Digite um preço: '))

print(f'O valor de {preco} + {valor} = {moeda.aumentar(preco, valor)}')
print(f'O valor de {preco} - {valor} = {moeda.diminuir(preco, valor)}')
print(f'O dobro de {preco} = {moeda.dobro(preco)}')
print(f'A medade de {preco} = {moeda.metade(preco)}')
