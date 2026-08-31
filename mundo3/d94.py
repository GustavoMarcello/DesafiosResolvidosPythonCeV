"""
EXERCÍCIO D94 - Unindo Dicionários e Listas
Crie um programa que:
1. Leia o nome, sexo e idade de várias pessoas
2. Guarde os dados de cada pessoa em um dicionário
3. Guarde todos os dicionários em uma lista
4. Mostre:
   a. Quantas pessoas foram cadastradas
   b. A média de idade do grupo
   c. Uma lista com todas as mulheres
   d. Uma lista com todas as pessoas com idade acima da média
"""

dados = []
totalPessoas = 0

while True:
    totalPessoas += 1
    nome = str(input(f'Digite o nome da pessoa {totalPessoas}: '))
    sexo = str(input(f'Digite o sexo [M/F] da pessoa {totalPessoas}: ')).upper()
    idade = int(input(f'Digite a idade da pessoa {totalPessoas}: '))

    pessoa = {'nome': nome, 'sexo': sexo, 'idade': idade}
    dados.append(pessoa)

    continuar = str(input('Deseja continuar [S/N]: ')).upper()
    if continuar == 'N':
        break

print(dados)

totalIdades = 0
for pessoa in dados:
   totalIdades += pessoa['idade']
mediaIdades = totalIdades / len(dados)

listaMulheres = []
maioresMedia = []
for pessoa in dados:
   if pessoa['idade'] > mediaIdades:
      maioresMedia.append(pessoa)

   if pessoa['sexo'] == 'F':
      listaMulheres.append(pessoa)

print(f'Foram cadastradas no total {len(dados)} pessoas')
print(f'A média de idades é de: {mediaIdades} anos')
print(f'Lista de Maiores q a média: {maioresMedia}')

if len(listaMulheres) == 0:
   print('Nenhuma mulher cadastrada')
else:
   print(f'Lista de Mulheres: {listaMulheres}')
