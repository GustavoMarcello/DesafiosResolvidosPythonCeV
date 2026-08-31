"""
EXERCÍCIO D89 - Boletim com listas compostas
Crie um programa que:
1. Leia o nome e a média de vários alunos, guardando tudo em uma lista composta
2. Pergunte ao usuário se ele deseja continuar [S/N]
3. No final, mostre um boletim contendo a média de cada um
4. Permita que o usuário possa visualizar as notas de cada aluno individualmente
"""

dados = []
numeroAluno = 0

while True:
    numeroAluno +=1
    nome = str(input(f'Digite o nome do aluno {numeroAluno}: '))
    nota1 = float(input(f'Digite a primeira nota do aluno {numeroAluno}: '))
    nota2 = float(input(f'Digite a segunda nota do aluno {numeroAluno}: '))
    media = (nota1 + nota2) / 2
    dados.append([nome, [nota1, nota2], media])

    continuar = str(input('Deseja continuar [S/N]: ')).upper()
    if continuar == 'N':
        break

print('-' * 30)
print('BOLETIM DOS ALUNOS'.center(30))
print('-' * 30)
for i, j in enumerate(dados):
    print(f'{i+1:<5} {j[0]:<20} {j[2]:>5.1f}')
print('-' * 30)

while True:
    visualizarNota = str(input('Deseja visualizar nota de algum aluno [S/N]: ')).upper()
    if visualizarNota == 'N':
            break

    aluno = int(input('Digite o número do aluno a visualizar notas: '))
    print(f'Nota 1: {dados[aluno-1][1][0]} || Nota 2: {dados[aluno-1][1][1]}')