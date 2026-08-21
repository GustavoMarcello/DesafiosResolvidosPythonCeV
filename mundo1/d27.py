"""
EXERCÍCIO D27 - Extrator de Primeiro e Último Nome
Crie um programa que:
1. Peça ao usuário para digitar seu nome completo
2. Limpe espaços em branco
4. Exiba o primeiro nome
5. Exiba o último nome
"""

nome = str(input('Digite seu nome completo: '))
listaNome = nome.strip().split()
print(f'Seu primeiro nome: {listaNome[0]}')
print(f'Seu último nome: {listaNome[-1]}')