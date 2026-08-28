"""
EXERCÍCIO D74 - Maior e Menor valor de uma tupla
Crie um programa que:
1. Gere uma tupla com 5 números inteiros aleatórios entre 1 e 50
2. Exiba a lista de números gerados
3. Exiba o maior e o menor valor da tupla
"""

from random import randint
valores = (
    randint(1, 50),
    randint(1, 50),
    randint(1, 50),
    randint(1, 50),
    randint(1, 50)
)

print(f'Valores sorteados: {valores}')
print(f'Maior valor sorteado: {max(valores)}')
print(f'Menor valor sorteado: {min(valores)}')