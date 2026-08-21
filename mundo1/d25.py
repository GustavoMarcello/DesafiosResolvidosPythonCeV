"""
EXERCÍCIO D25 - Analisador de Palavra em Frase
Crie um programa que:
1. Peça ao usuário digitar seu nome completo
2. Analise se contém o nome "SILVA" (independente de maiúsculas ou minúsculas)
"""
nome = str(input('Digite seu nome completo: '))
upperNome = nome.upper()

print(f'Nome da cidade digitado: {upperNome}')
print(f'Seu nome contém "SILVA"? {'SILVA' in upperNome}')