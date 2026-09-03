"""
EXERCÍCIO D109  - Melhorando o módulo moeda
1. Refatore o as funções de moeda.py para que elas aceitem um parâmetro a mais,
2. Informe se o valor retornado por elas vai ser ou não formatado pela função moeda()
"""

import moeda

valor = 12

preco = float(input('Digite um preço: '))

print(f'O valor de {preco} + {valor} = {moeda.aumentar(preco, valor, True)}')
print(f'O valor de {preco} - {valor} = {moeda.diminuir(preco, valor, True)}')
print(f'O dobro de {preco} = {moeda.dobro(preco, True)}')
print(f'A medade de {preco} = {moeda.metade(preco, True)}')