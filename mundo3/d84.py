"""
EXERCÍCIO D84 - Lista de pessoas e pesos
Crie um programa que:
1. Leia o nome e o peso de várias pessoas, guardando tudo em uma lista
2. Pergunte ao usuário se ele deseja continuar [S/N]
3. No final, mostre:
    a) Quantas pessoas foram cadastradas
    b) A pessos mais pesada
    c) A pessoa mais leve
"""
indice = 1
totalPessoas = []

while True:
    nome = str(input(f'Digite o Nome da pessoa {indice }: '))
    peso = float(input(f'Digite o Peso da pessoa {indice}: '))

    indice += 1
    dados = [nome, peso]
    totalPessoas.append(dados)

    continuar = str(input('Deseja continuar [S/N]: ')).upper()
    if continuar == 'N':
        break

print(f'\nTotal de cadastros: {len(totalPessoas)} pessoas')

maiorPeso = totalPessoas[0][1]
for pessoa in totalPessoas:
    if pessoa[1] > maiorPeso:
        maiorPeso = pessoa[1]

print('Pessoa mais pesada:')
for pessoa in totalPessoas:
    if pessoa[1] == maiorPeso:
        print(f'{pessoa[0]} - {pessoa[1]:.2f} kg')


menorPeso = totalPessoas[0][1]
for pessoa in totalPessoas:
    if pessoa[1] < menorPeso:
        menorPeso = pessoa[1]

print('Pessoa mais leve:')
for pessoa in totalPessoas:
    if pessoa[1] == menorPeso:
        print(f'{pessoa[0]} - {pessoa[1]:.2f} kg')
