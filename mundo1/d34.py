"""
EXERCÍCIO D33 - Aumento de Salário Progressivo por Faixa
Crie um programa que:
1. Peça ao usuário para digitar o salário de um funcionário
2. Aplique aumento conforme a faixa salárial:
   - Se salário <= R$1250: aumento de 15%
   - Se salário > R$1250: aumento de 10%
3. Calcule o novo salário
4. Exiba o salário original, valor do aumento e novo salário
"""

salario = float(input('Digite o valor do salário: '))

if salario <= 1250:
    aumento = salario * 1.15
else:
    aumento = salario * 1.1

print(f'O Salário foi de R$ {salario} para R$ {aumento}')