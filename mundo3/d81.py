"""
EXERCÍCIO D81 - Extraindo dados de uma lista
Crie um programa que:
1. Leia vários números inteiros pelo teclado e guarde-os em uma lista
2. Pergunte ao usuário se ele deseja continuar [S/N]
3. No final, mostre:
    a) Quantos números foram digitados
    b) A lista de valores, ordenada de forma decrescente
    c) Se o valor 5 está ou não presente na lista
"""

valores = []

while True:
    valores.append(int(input('Digite um valor: ')))

    continuar = str(input('Deseja continuar [S/N]: ')).upper()
    if continuar == 'N':
        break

valores.sort(reverse=True)
print(f'Foram digitados {len(valores)} valores')
print(f'Valores digitados em ordem decrescente: {valores}')
print(f'O valor 5 foi digitado?: {5 in valores}')