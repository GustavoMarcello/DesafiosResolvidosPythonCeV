"""
EXERCÍCIO D50 - Somador de Números Pares
Crie um programa que:
1. Peça ao usuário para digitar 6 números inteiros
2. Some apenas os números pares
3. Ao final, exiba a soma dos números pares apenas
"""

soma = 0

for i in range(0, 6):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        soma+= n
print(f'A soma dos números pares digitados = {soma}')