"""
EXERCÍCIO D16 - Parte Inteira de um Número
Crie um programa que:
1. Importe o módulo math
2. Peça ao usuário para digitar um número decimal
3. Use a função math.trunc() para obter a parte inteira
4. Exiba o número digitado e sua porção inteira
"""

import math

n = float(input('Digite um número decimal: '))
print(f'A parte inteira digitada é de {math.trunc(n)}')