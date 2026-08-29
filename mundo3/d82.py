"""
EXERCÍCIO D82 - Dividindo valores em várias listas
Crie um programa que:
1. Leia vários números inteiros pelo teclado
2. Pergunte ao usuário se ele deseja continuar [S/N]
3. Divida-os em duas listas: uma com os valores pares e outra com os ímpares
4. Exiba as três listas
"""

valores = []
pares = []
impares = []

while True:
    n = int(input('Digite um valor: '))
    valores.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

    continuar = str(input('Deseja continuar [S/N]: ')).upper()
    if continuar == 'N':
        break

print(f'Lista total: {valores}')
print(f'Lista pares: {pares}')
print(f'Lista impares: {impares}')