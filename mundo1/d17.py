"""
EXERCÍCIO D17 - Cálculo da Hipotenusa (Teorema de Pitágoras)
Crie um programa que:
1. Importe o módulo math
2. Peça ao usuário para digitar o comprimento dos dois catetos de um triângulo retângulo
3. Use a função math.hypot() para calcular a hipotenusa
4. Exiba o valor da hipotenusa com 2 casas decimais
"""

import math
cat1 = float(input('Digite o comprimento do cateto 1: '))
cat2 = float(input('Digite o comprimento do cateto 2: '))

print(f'O comprimento total da hipotenusa é de {math.hypot(cat1, cat2)}')