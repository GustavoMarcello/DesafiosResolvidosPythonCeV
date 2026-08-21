"""
EXERCÍCIO D14 - Conversão de Temperatura (Celsius para Fahrenheit)
Crie um programa que:
1. Peça ao usuário para digitar uma temperatura em graus Celsius
2. Converta para Fahrenheit usando a fórmula: F = (C * 9/5) + 32
3. Exiba a temperatura em ambas as escalas
"""

celcius = float(input('Digite a temperatura em graus Celsius: '))
fahrenheit = (celcius * 9 / 5) + 32

print(f'A conversão de {celcius:.2f} °C = {fahrenheit:.2f} °F')