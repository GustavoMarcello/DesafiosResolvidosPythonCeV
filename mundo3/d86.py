"""
EXERCÍCIO D86 - Matriz em Python
Crie um programa que:
1. Leia valores para uma matriz 3x3
2. Exiba a matriz formatada
"""

matriz = [[0,0,0],[0,0,0],[0,0,0]]

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite o valor [{linha}, {coluna}]: '))

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]}]', end=' ')
    print()