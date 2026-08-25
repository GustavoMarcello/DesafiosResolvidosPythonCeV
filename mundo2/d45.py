"""
EXERCÍCIO D45 - Sorteador de Jogo de Pedra, Papel, Tesoura
Crie um programa que:
1. Importe o módulo random
2. Permita que o usuário escolha: Pedra, Papel ou Tesoura
3. O computador escolha aleatoriamente
4. Defina as regras:
   - Tesoura vence Papel
   - Papel vence Pedra
   - Pedra vence Tesoura
5. Exiba a escolha do usuário, do computador e declara o vencedor
"""
from random import choice

opcoes = ['PEDRA', 'PAPEL', 'TESOURA']

print('Vamos jogar PEDRA, PAPEL, TESOURA')
escolha = str(input('Digite sua escolha: ')).upper()

rival = choice(opcoes)

if escolha == rival:
    print(f'Você \033[30m{escolha}\033[m X \033[30m{rival}\033[m Rival - \033[30mEMPATE\033[m')
elif escolha == 'PEDRA' and rival == 'PAPEL':
    print(f'Você \033[33m{escolha}\033[m X \033[34m{rival}\033[m Rival - \033[31mVOCÊ PERDEU\033[m')
elif escolha == 'PEDRA' and rival == 'TESOURA':
    print(f'Você \033[33m{escolha}\033[m X \033[35m{rival}\033[m Rival - \033[32mVOCÊ GANHOU\033[m')
elif escolha == 'PAPEL' and rival == 'PEDRA':
    print(f'Você \033[34m{escolha}\033[m X \033[33m{rival}\033[m Rival - \033[32mVOCÊ GANHOU\033[m')
elif escolha == 'PAPEL' and rival == 'TESOURA':
    print(f'Você \033[34m{escolha}\033[m X \033[35m{rival}\033[m Rival - \033[31mVOCÊ PERDEU\033[m')
elif escolha == 'TESOURA' and rival == 'PEDRA':
    print(f'Você \033[35m{escolha}\033[m X \033[33m{rival}\033[m Rival - \033[31mVOCÊ PERDEU\033[m')
elif escolha == 'TESOURA' and rival == 'PAPEL':
    print(f'Você \033[35m{escolha}\033[m X \033[34m{rival}\033[m Rival - \033[32mVOCÊ GANHOU\033[m')
else:
    print('Escolha digitada inválida')