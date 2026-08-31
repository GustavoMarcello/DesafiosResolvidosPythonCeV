"""
EXERCÍCIO D93 - Cadastro de Jogador de Futebol
Crie um programa que:
1. Leia o nome do jogador e quantas partidas ele jogou
2. Leia o número de gols feitos em cada partida
3. Guarde tudo em um dicionário, incluindo o total de gols feitos durante o campeonato
"""

dados = {}
totalGols = 0

dados['nome'] = str(input('Digite o nome do jogador: '))
dados['qtdPartidas'] = int(input('Digite a quantidade de partidas feitas: '))

for i in range(1, dados['qtdPartidas']+1):
    gols = int(input(f'Quantos gols na partida {i}: '))
    totalGols +=gols

dados['totalGols'] = totalGols
print(dados)