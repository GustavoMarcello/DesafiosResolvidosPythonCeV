"""
EXERCÍCIO D71 - Simulador de Caixa Eletrônico
Crie um programa que:
1. Peça ao usuário o valor a ser sacado (número inteiro)
2. Calcule o número mínimo de cédulas necessárias para o saque
3. Exiba a quantidade de cada tipo de cédula

Obs: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
"""

valor = int(input('Digite o valor inteiro a ser sacado: '))

qtdCinquenta = valor // 50
restoCinquenta = valor % 50

qtdVinte = restoCinquenta // 20
restoVinte = restoCinquenta % 20

qtdDez = restoVinte // 10
restoDez = restoVinte % 10

print(f'Notas sacadas: {qtdCinquenta} cinquenta, {qtdVinte} vinte, {qtdDez} dez, {restoDez} um')
