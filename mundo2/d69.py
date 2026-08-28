"""
EXERCÍCIO D69 (melhorado) - Analizando informações de pessoas
Crie um programa que:
1. Leia leia informações de N pessoas sendo:
    - Nome,
    - Idade,
    - Sexo,
2. Ao final demonstre:
    - A média de idade do grupo,
    - O nome do Homem mais velho,
    - Quantas Mulheres tem menos de 20 anos,
3. O programa deverá sempre perguntar se o usuário deseja continuar [S/N] e finalizar com "N"
"""


qdtPessoas = 1
somaIdade = 0
idadeHomemVelho = 0
homemMaisVelho = ''
mulheresMenoresVinte = 0

while True:
    nome = str(input(f'Digite o Nome da pessoa {qdtPessoas}: '))
    idade = int(input(f'Digite o Idade da pessoa {qdtPessoas}: '))
    sexo = str(input(f'Digite o Sexo da pessoa {qdtPessoas}: ')).upper()

    somaIdade += idade
    qdtPessoas += 1

    if sexo == 'M' and idade > idadeHomemVelho:
        idadeHomemVelho = idade
        homemMaisVelho = nome
    else:
        if idade < 20:
            mulheresMenoresVinte += 1

    continuar = str(input('Deseja continuar [S/N]: ')).upper()
    if continuar == 'N':
        break


mediaIdade = somaIdade / qdtPessoas

print(f'Média de Idade: {mediaIdade}')
print(f'Homem mais velho: {homemMaisVelho}')
print(f'Quantidade de mulheres menores de 20 anos: {mulheresMenoresVinte}')