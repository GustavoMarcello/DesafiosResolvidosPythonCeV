"""
EXERCÍCIO D42 - Analizador de triangulos
Crie um programa que:
1. Leia o comprimento de três segmentos de reta
2. Exiba se eles podem formar um triângulo
3. Caso possam formar um triângulo, classifique-o como:
   - Equilátero: todos os lados iguais
   - Isósceles: dois lados iguais
   - Escaleno: todos os lados diferentes
"""

a = float(input('Digite o primeiro lado do triângulo: '))
b = float(input('Digite o segundo lado do triângulo: '))
c = float(input('Digite o terceiro lado do triângulo: '))

if a < (b + c) and b < (a + c) and c < (a + b):
   if a == b and b == c:
      print('É um triângulo EQUILÁTERO')
   elif a != b and a != c and b != c:
      print('É um triângulo ESCALENO')
   else:
      print('É um triângulo ISOSSELES')
else:
    print('Não é um triângulo')