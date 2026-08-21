"""
EXERCÍCIO D34 - Comparador de Números
Crie um programa que:
1. Peça ao usuário para digitar três números diferentes
2. Identifique qual é o maior e qual é o menor
3. Exiba o maior e o menor número digitado

obs*: Use apenas condicional
"""

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))

menor = n1

if n1>n2 and n1>n3:
    maior = n1
    if n2>n3:
        menor = n3
    else:
        menor = n2
if n2>n1 and n2>n3:
    maior = n2
    if n1>n3:
        menor = n3
    else:
        menor = n1
if n3>n1 and n3>n2:
    maior = n3
    if n1>n2:
        menor = n2
    else:
        menor = n1

print(f'Maior = {maior} | Menor = {menor}')