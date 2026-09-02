"""
EXERCÍCIO D108 - Formatando moedas em Python
Crie um programa que:
1. Crie uma função adicional no modulo 'moeda' chamada moeda()
2. Essa função deverá formatar valores monetários em R$ com dois digitos após a vírgula
"""

import moeda

valor = 12

preco = float(input('Digite um preço: '))

print(f'O valor de {preco} + {valor} = {moeda.moeda(moeda.aumentar(preco, valor))}')
print(f'O valor de {preco} - {valor} = {moeda.moeda(moeda.diminuir(preco, valor))}')
print(f'O dobro de {preco} = {moeda.moeda(moeda.dobro(preco))}')
print(f'A medade de {preco} = {moeda.moeda(moeda.metade(preco))}')