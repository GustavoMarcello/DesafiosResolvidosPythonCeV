"""
EXERCÍCIO D6 - Dobro, Triplo e Raiz Quadrada
Crie um programa que:
1. Peça ao usuário para digitar um número
2. Calcule o dobro, o triplo e a raiz quadrada
3. Exiba todos os resultados com 2 casas decimais
"""

n = int(input('Digite um valor inteiro: '))
print(f'O dobro de {n} é {n*2:.2f}')
print(f'O triplo de {n} é {n*3:.2f}')
print(f'O raíz de {n} é {n**(1/2):.2f}')