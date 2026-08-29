"""
EXERCÍCIO D88 - Jogo da Mega Sena
Crie um programa que:
1. Gere 6 números aleatórios entre 1 e 60 para cada jogo
2. Permita ao usuário escolher quantos jogos deseja gerar
3. Exiba os jogos gerados
"""

from random import randint

jogo = []

qtdJogos = int(input('Digite quantos jogos da Megasena você deseja sortear: '))

for i in range(0, qtdJogos):
    for j in range(0, 6):
        valorSorteado = randint(1, 60)
        jogo.append(valorSorteado)
    print(jogo)
    jogo.clear()