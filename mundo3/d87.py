"""
EXERCÍCIO D87 - Matriz em Python
Crie um programa que:
1. Leia valores para uma matriz 3x3
2. Exiba a matriz formatada
3. Ao final mostre:
    a) A soma de todos os valores pares digitados
    b) A soma dos valores da terceira coluna
    c) O maior valor da segunda linha
"""

matriz = [[0,0,0],[0,0,0],[0,0,0]]
somaPares = 0
somaColunaTres = 0
somaLinhaDois = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        n = int(input(f'Digite o valor [{linha}, {coluna}]: '))
        matriz[linha][coluna] = n

        if n % 2 == 0:
            somaPares += n

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]}]', end=' ')

        if linha == 1:
            somaLinhaDois += matriz[linha][coluna]

        if coluna == 2:
            somaColunaTres += matriz[linha][coluna]

    print()

print(f'Soma valores pares: {somaPares}')
print(f'Soma coluna três: {somaColunaTres}')
print(f'Soma linha dois: {somaLinhaDois}')