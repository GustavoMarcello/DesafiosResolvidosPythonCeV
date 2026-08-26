"""
EXERCÍCIO D54 - Analise Maior e menor de idade
Crie um programa que:
1. Leia o ano de nascimento de 7 pessoas
2. Ao final mostre:
    -  Quantas são maiores de idade,
    -  Quantas são menores de idade,
"""

qdtPessoas = 7
anoAtual = 2026
maiores = []
menores = []

for i in range(1, qdtPessoas+1):
    anoNascimento = int(input(f'Digite o ano de nascimento da pessoa {i}: '))
    if anoAtual - anoNascimento > 17:
        maiores.append(anoNascimento)
    else:
        menores.append(anoNascimento)

print(f'Anos maiores de idade: {maiores}')
print(f'Anos menores de idade: {menores}')