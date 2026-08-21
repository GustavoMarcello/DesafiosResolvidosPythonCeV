"""
EXERCÍCIO D30 - Verificador de Número Par ou Ímpar
Crie um programa que:
1. Peça ao usuário para digitar um número inteiro
2. Verifique se é divisível por 2
3. Exiba o resultado se é par ou ímpar
"""

n = int(input('Digite um número inteiro: '))

if n%2 == 0:
    print(f'{n} é par')
else:
    print(f'{n} é ímpar')