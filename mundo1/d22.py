"""
EXERCÍCIO D22 - Análise de Nome Completo
Crie um programa que:
1. Peça ao usuário para digitar seu nome completo
2. Processe o nome: remova espaços, converta para maiúsculas e minúsculas
3. Conte o número total de caracteres (sem espaços)
4. Extraia o primeiro nome e conte seus caracteres
5. Exiba todas essas informações
"""

nome = str(input('Digite seu nome completo: '))

print(f'Seu nome sem espaços: {nome.replace(' ', '')}')
print(f'Seu nome em maiúsculo: {nome.upper()}')
print(f'Seu nome em minúsculo: {nome.lower()}')
print(f'Seu nome tem {len(nome)} caracteres')
print(f'Seu primeiro nome é: {nome.split()[0]}')