"""
EXERCÍCIO D38 - Comparador de Dois Números
Crie um programa que:
1. Peça ao usuário para digitar Dois números diferentes
2. Identifique o maior e o menor
3. Exiba qual é maior, menor ou se são iguais
"""

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

menor = n1

if n1>n2:
    print(f'Maior = {n1} | Menor = {n2}')
elif n2>n1:
    print(f'Maior = {n2} | Menor = {n1}')
else:
    print(f'{n1} = {n2}')