"""
EXERCÍCIO D26 - Analisador de Letra em Frase
Crie um programa que:
1. Peça ao usuário para digitar uma frase
2. Conte quantas vezes a letra 'A' aparece
3. Encontre a posição da primeira letra 'A'
4. Encontre a posição da última letra 'A'
5. Exiba todos os resultados
"""

frase = input('Digite uma frase qualquer: ')

upperFrase = frase.upper()
print(f'Sua frase contem {upperFrase.count('A')}  letras "A"')
print(f'A primeira letra "A" aparece na posição: {upperFrase.find('A')+1}')
print(f'A última letra "A" aparece na posição: {upperFrase.rfind('A')+1}')