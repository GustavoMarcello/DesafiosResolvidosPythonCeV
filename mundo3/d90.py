"""
EXERCÍCIO D90 - Dicionário em Python
Crie um programa que:
1. Leia o nome e a média de vários alunos, guardando tudo em um dicionário
2. Pergunte ao usuário se ele deseja continuar [S/N]
3. No final, mostre o conteúdo da estrutura na tela
"""


dados = []
numeroAluno = 0

while True:
    numeroAluno +=1
    nome = str(input(f'Digite o nome do aluno {numeroAluno}: '))
    media = float(input(f'Digite a média do aluno {numeroAluno}: '))
    dados.append({'nome': nome, 'media': media})

    continuar = str(input('Deseja continuar [S/N]: ')).upper()
    if continuar == 'N':
        break

print('-' * 30)
print('BOLETIM DOS ALUNOS'.center(30))
print('-' * 30)
for i, j in enumerate(dados):
    print(f'{i+1:<5} {j['nome']:<20} {j['media']:>5.1f}')
print('-' * 30)