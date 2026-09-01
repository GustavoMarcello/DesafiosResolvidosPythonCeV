"""
EXERCÍCIO D96 - Função que calcula Área
Crie um programa que:
1. Crie uma função que receba as dimensões de um terreno retangular (largura e comprimento) 
2. Mostre a área do terreno
"""
def calcArea( largura, comprimento):
    return largura* comprimento


largura = float(input('Digite a largura do terreno: '))
comprimento = float(input('Digite o comprimento do terreno: '))

area = calcArea(largura, comprimento)
print(f'A área total do terreno é {area} m²')

    