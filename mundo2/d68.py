"""
EXERCÍCIO D68 - Jogo Par ou ímpar
Crie um programa que:
1. Jogue "Par ou Ímpar" com o usuário
2. O programa devera finalizar quando o usuário perder, demonstrando a quantidade seguida de vitórias
"""

from random import randint

qtdVitorias = 0

while True:
    escolha = str(input('Par ou ímpar [P/I]: ')).upper()
    nUsuario = int(input('Digite seu número: '))

    nCompu = randint(1,2)
    resto = (nUsuario+nCompu)%2

    if resto == 1 and escolha == 'P' or resto == 0 and escolha == 'I':
        print(f'Escolha da máquina: {nCompu}')
        print(f'Você perdeu, ganhando {qtdVitorias} vezes seguidas')
        break

    qtdVitorias += 1
    print(f'Escolha da máquina: {nCompu}')
    print(f'Você Ganhou! Vamos outra vez!\n')
