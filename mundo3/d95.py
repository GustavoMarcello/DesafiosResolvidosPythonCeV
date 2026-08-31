"""
EXERCÍCIO D95 - Aprimorando os Dicionários
Crie um programa que:
1. Aprimore o desafio 93 para que ele funcione com vários jogadores
"""
dados = []

while True:
    nome = str(input('Digite o nome do jogador: '))
    qtdPartidas = int(input('Digite a quantidade de partidas feitas: '))

    totalGols = 0
    golPartida = []
    for i in range(1, qtdPartidas+1):
        gols = int(input(f'Quantos gols na partida {i}: '))
        golPartida.append(gols)
        totalGols +=gols

    dados.append({'nome': nome, 'qtdPartidas': qtdPartidas, 'totalGols': totalGols, 'golPartida': golPartida})

    continuar = str(input('Deseja continuar [S/N]: ')).upper()
    if continuar == 'N':
        break

print('-' *60)
print('JOGADORES'.center(60))
print('-' * 60)
print(f"{'Nome':<20}{'qtdPartidas':<15}{'totalGols':<15}{'golPartida':<20}")
print('-' * 60)
for jogador in dados:
    print(f'{jogador['nome']:<20}{jogador['qtdPartidas']:<15}{jogador['totalGols']:<15}{str(jogador['golPartida']):<20}')
print('-' * 60)