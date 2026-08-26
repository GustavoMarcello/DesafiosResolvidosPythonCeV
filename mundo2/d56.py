"""
EXERCÍCIO D56 - Analizando informações de pessoas
Crie um programa que:
1. Leia leia informações de 4 pessoas sendo:
    - Nome,
    - Idade,
    - Sexo,
2. Ao final demonstre:
    - A média de idade do grupo,
    - O nome do Homem mais velho,
    - Quantas Mulheres tem menos de 20 anos,
"""

qdtPessoas = 4
somaIdade = 0
idadeHomemVelho = 0
homemMaisVelho = ''
mulheresMenoresVinte = 0

for i in range(1, qdtPessoas+1):
    nome = str(input(f'Digite o Nome da pessoa {i}: '))
    idade = int(input(f'Digite o Idade da pessoa {i}: '))
    sexo = str(input(f'Digite o Sexo da pessoa {i}: ')).upper()

    somaIdade += idade

    if sexo == 'M' and idade > idadeHomemVelho:
        idadeHomemVelho = idade
        homemMaisVelho = nome
    else:
        if idade < 20:
            mulheresMenoresVinte += 1

mediaIdade = somaIdade / qdtPessoas

print(f'Média de Idade: {mediaIdade}')
print(f'Homem mais velho: {homemMaisVelho}')
print(f'Quantidade de mulheres menores de 20 anos: {mulheresMenoresVinte}')