"""
EXERCÍCIO D23 - Divisor de Dígitos
Crie um programa que:
1. Peça ao usuário para digitar um número inteiro de 4 dígitos
2. Separe e exiba cada dígito com seu nome:
   - Dígito na posição 3 = unidade
   - Dígito na posição 2 = dezena
   - Dígito na posição 1 = centena
   - Dígito na posição 0 = milhar
"""

num = input('Digite um número de 4 unidades: ')

print(f'Unidade: {num[3]}')
print(f'Dezena: {num[2]}')
print(f'Centena: {num[1]}')
print(f'Milhar: {num[0]}')