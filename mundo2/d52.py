"""
EXERCÍCIO D52 - Analisador de Número Primo
Crie um programa que:
1. Peça ao usuário para digitar um número
2. Verifique se o número é primo
3. Se for primo, exiba "X é um número primo"
4. Se não for, exiba seus divisores além de 1 e ele mesmo
"""

n = int(input("Digite um número para verificar se é primo: "))
divisores = []

for i in range(1, n+2):
    if n % i == 0:
        divisores.append(i)

if len(divisores) == 2:
    print(f'{n} é primo, divisível apenas por {n} e 1')
else:
    print(f'{n} não é primo, divisível por {divisores}')