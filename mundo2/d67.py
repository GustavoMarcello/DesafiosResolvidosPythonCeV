"""
EXERCÍCIO D67 - Tábuada 3.0
Crie um programa que:
1. Gere a tabuada de 1 até 10 de um valor inteiro inserido pelo usuário
2. Pergunte um novo valor e gere novamente a tabuáda.
3. O programa devera finalizar ao input de um valor negativo
"""

while True:
    n = int(input('Digite um número para tabuada ou negativo para encerrar: '))
    
    if n < 0:
        break

    for i in range (1, 11):
        print(f'{n} X {i} = {n*i}')
    