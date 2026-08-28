"""
EXERCÍCIO D70 - Analizando produtos
Crie um programa que:
1. Leia leia informações de N produtos sendo:
    - Nome,
    - Valor,
2. Ao final demonstre:
    - Valor total dos produtos,
    - O nome do produto mais barato,
    - Quantos produtos têm valor acima de R$ 1000,
3. O programa deverá sempre perguntar se o usuário deseja continuar [S/N] e finalizar com "N"
"""


qdtProduto = 1
qtdAcimaMil = 0
somaValor = 0
valorProdutoMaisCaro = 0
produtoMaisCaro = ''

while True:
    nome = str(input(f'Digite o Nome do produto {qdtProduto}: '))
    valor = float(input(f'Digite o Valor do produto {qdtProduto}: '))

    somaValor += valor
    qdtProduto += 1

    if valor > valorProdutoMaisCaro:
        valorProdutoMaisCaro = valor
        produtoMaisCaro = nome

    if valor > 1000:
        qtdAcimaMil += 1

    continuar = str(input('Deseja continuar [S/N]: ')).upper()
    if continuar == 'N':
        break


print(f'Valor total dos produtos: {somaValor}')
print(f'Produto mais caro: {produtoMaisCaro}')
print(f'Quantidade de produtos acima de R$ 1000: {qtdAcimaMil}')