"""
EXERCÍCIO D48 - Somador de Ímpares múltiplos de 3
Crie um programa que:
1. Demonstre o número todal de números ímpares múltiplos de 3 entre 1 e 500
2. Exiba a soma desses números
"""

print('Números ímpares múltiplos de 3 entre 1 e 500')
soma = 0
for i in range(1, 500, 2):
    if i%3 == 0:
        soma += i
        print(i)

print(f'A soma dos números: {soma}')