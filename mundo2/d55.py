"""
EXERCÍCIO D55 - Maior e menor peso
Crie um programa que:
1. Leia o peso de 5 pessoas
2. Ao final demonstre o peso da maior e da menor pessoa
"""

qdtPessoas = 5
anoAtual = 2026
listaPesos = []

for i in range(1, qdtPessoas+1):
    peso = int(input(f'Digite o peso da pessoa {i}: '))
    listaPesos.append(peso)

listaPesos.sort()
print(listaPesos)
print(f'Maior peso: {listaPesos[-1]}')
print(f'Menor peso: {listaPesos[0]}')