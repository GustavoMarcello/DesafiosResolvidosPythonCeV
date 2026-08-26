"""
EXERCÍCIO D53 - Verificador de Palíndromo
Crie um programa que:
1. Peça ao usuário para digitar uma palavra ou frase
2. Remova espaços e converta para minúsculas
3. Verifique se a palavra é um palíndromo (lê-se igual de trás para frente)
4. Compare a frase com sua versão invertida
5. Exiba se é um palíndromo ou não
"""

frase = str(input('Digite uma frase: ')).strip().upper()
fraseFormatada = frase.replace(' ', '')
fraseInvertida = ''

for i in range(len(fraseFormatada)-1, -1, -1):
    fraseInvertida += fraseFormatada[i]

if fraseInvertida == fraseFormatada:
    print(f'{frase} é um PALINDROMO')
else:
    print(f'NÃO é um PALINDROMO')