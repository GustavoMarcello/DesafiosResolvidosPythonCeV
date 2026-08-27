"""
EXERCÍCIO D60 - Cálculo Fatorial
Crie um programa que:
1. Leia um número inteiro
2. Calcule seu fatorial

Ex: 4! = 4 * 3 * 2 * 1 = 24
Obs*: Use while
"""

fatorial = int(input('Digite um número: '))
i = fatorial
resultado = f'{i} '

while i > 1:
    i -= 1
    resultado += f'* {i} '
    fatorial *= i

print(f'{resultado} = {fatorial}')
