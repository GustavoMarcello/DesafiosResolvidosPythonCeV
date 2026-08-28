"""
EXERCÍCIO D77 - Contando palavras em uma Tupla
Crie um programa que:
1. Crie uma tupla com várias palavras
2. Mostre para cada palavra suas vogais
"""

palavras = (
    "python",
    "java",
    "javascript",
    "java",
    "c",
)

vogais = "aeiou"

for palavra in palavras:
    print(f"\nPalavra: {palavra}")
    print("Vogais:", end=" ")

    for letra in palavra:
        if letra in vogais:
            print(letra, end=" ")

print()