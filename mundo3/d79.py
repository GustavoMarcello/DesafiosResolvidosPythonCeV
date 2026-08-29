"""
EXERCÍCIO D79 - Valores Únicos em uma Lista
Crie um programa que:
1. Leia vários números inteiros pelo teclado e guarde-os em uma lista
2. Caso o número já exista na lista, ele não será adicionado
3. No final, serão exibidos todos os valores únicos digitados, em ordem crescente
4. Pergunte ao usuário se ele deseja continuar [S/N]
"""

valores = []

while True:
    n = int(input('Digite um valor: '))
    if n not in valores:
        valores.append(n)

    continuar = str(input('Deseja continuar [S/N]: ')).upper()
    if continuar == 'N':
        break

valores.sort()
print(f'Valores únicos digitados: {valores}')