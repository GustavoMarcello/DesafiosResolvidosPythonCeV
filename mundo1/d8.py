"""
EXERCÍCIO D8 - Conversão de Unidades de Comprimento
Crie um programa que:
1. Peça ao usuário para digitar um valor em metros
2. Converta para centímetros e milímetros
3. Exiba as três medidas
"""

m = float(input(f'Digite um valor em metros: '))
cm = m * 100
mm = m * 1000

print(f'Convertendo para centimetros: {cm:.2f} cm')
print(f'Convertendo para milimetros: {mm:.2f} mm')