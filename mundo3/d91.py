"""
EXERCÍCIO D91- Jogo de dados em Python
Crie um programa que:
1. Importe o módulo random
2. Gere 4 valores de um dado (1 a 6) para cada jogador
3. Guarde esses valores em um dicionario
4. Ordene os jogadores por ordem de maior pontuação
5. Demonstre o ranking do jogo
"""

from random import randint

totalPlayers = 6
qtdValores = 4
jogadores = []

for i in range(0, totalPlayers):
    valoresJogador = []
    for j in range(0, qtdValores):
        valor = randint(1, 6)
        valoresJogador.append(valor)
    total = sum(valoresJogador)
    jogadores.append({f'valores': valoresJogador, 'total': total})

jogadores.sort(key=lambda jogador: jogador['total'], reverse=True)

print('-' * 30)
print('VALORES DOS JOGADORES'.center(30))
print('-' * 30)
for i, j in enumerate(jogadores):
    print(f'Jogador {i+1}: {j['valores']} Total: {j['total']}')
print('-' * 30)
