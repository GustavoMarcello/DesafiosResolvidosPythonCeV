"""
EXERCÍCIO D85 - Listas com pares e ímpares
Crie um programa que:
1. Leia 7 números inteiros pelo teclado
2. Separe-os em duas listas: uma com os valores pares e outra com os ímpares
3. Ao final, exiba as duas listas em ordem crescente
"""

pares = []
impares = []
fim = 7

for i in range(0, fim):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

pares.sort()
impares.sort()

print(f'Lista pares: {pares}')
print(f'Lista impares: {impares}')