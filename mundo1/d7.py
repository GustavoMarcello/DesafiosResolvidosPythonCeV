"""
EXERCÍCIO D7 - Média Aritmética de Duas Notas
Crie um programa que:
1. Peça ao usuário para digitar duas notas
2. Calcule a média aritmética das notas
3. Exiba a média com 2 casas decimais
"""

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

print(f'A media das notas é: {media:.2f}')
