"""
EXERCÍCIO D103 - Função para ficha de jogador
Crie um programa que:
1. Contenha uma função que receba como parâmetro o nome de um jogador e quantos gols ele marcou
2. A função deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente  
"""

def infoJogador(nome='', gols=0):
    if nome=='':
        nome = '<desconhecido>'
    if not gols:
        gols = 0

    print(f'O jogador {nome} marcou {gols} gols')


nome = str(input('Digite o nome do jogador: '))
gols = input('Digite a quantidade de gols do jogador: ')

infoJogador(nome, gols)