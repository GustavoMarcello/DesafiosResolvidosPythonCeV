"""
EXERCÍCIO D11 - Cálculo de Tinta para Pintar Parede
Crie um programa que:
1. Peça ao usuário para digitar a largura e altura da parede em metros
2. Calcule a área da parede
3. Calcule a quantidade de tinta necessária (1 litro pinta 2 metros quadrados)
4. Exiba a área e a quantidade de tinta com 2 casas decimais
"""

altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))

area = altura * largura
qtdTinta = area / 2

print(f'Serão necessários {qtdTinta:.2f} L de tinta para pintar {area:.2f} m² de parede')
