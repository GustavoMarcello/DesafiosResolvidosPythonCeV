"""
EXERCÍCIO D58 - Jogo de Advinhação v2.0
Crie um programa que:
1. Importe o módulo random
2. Gere um número aleatório entre 0 e 10 usando random.randint()
3. Peça ao usuário para digitar um número nesse mesmo intervalo
4. Verifique se o usuário acertou ou errou:
   - Se acertou: exiba "Parabéns! Você acertou!"
   - Se errou: solicite um novo valor
5. Ao Final demonstre quantos palpites foram necessários para o acerto
"""

from random import randint

sorteado = randint(1, 10)
escolha = 0
tentativas =0

while escolha != sorteado:
   tentativas += 1
   valor = int(input('Digite um valor entre 1 e 10: '))
   if valor != sorteado:
      print(f'Você errou, tente novamente')
   else:
      escolha = valor
      print(f'Correto em {tentativas} tentativas, o valor sorteado foi {sorteado}')
   