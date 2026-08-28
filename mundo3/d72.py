"""
EXERCÍCIO D72 - Conversor de Número para Extenso
Crie um programa que:
1. Peça ao usuário para digitar um número entre 0 e 5
2. Converta o número para extenso em português
3. Exiba o número por extenso

Obs: Use uma tupla para armazenar os nomes dos números.
"""

numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco')

n = int(input('Digite um número entre 0 e 5: ' ))
print(f'Número digitado por extenso: {numeros[n]}')