"""
EXERCÍCIO D4 - Identificar Tipo de Dado
Crie um programa que:
1. Peça ao usuário para digitar algo
2. Identifique qual é o tipo primitivo do valor digitado
3. Exiba o tipo de dado
"""

algo = input('Digite algo: ')
print(f'O tipo primitivo do que foi digitado é: {type(algo)}')
print(f'usando funçoes tipo isspace: {algo.isspace()}')
print(f'usando funçoes tipo isnumeric: {algo.isnumeric()}')