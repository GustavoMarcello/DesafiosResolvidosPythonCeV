"""
EXERCÍCIO D13 - Aumento de Salário de 15%
Crie um programa que:
1. Peça ao usuário para digitar o salário de um funcionário
2. Calcule o aumento de 15%
3. Exiba o salário original e o novo salário com aumento
"""

salario = float(input('Digite o valor em reais do salario atual: '))
print(f'15% de aumento para R${salario:.2f}: R${(salario*1.15):.2f}')