"""
EXERCÍCIO D104 - Função para validação de dados
Crie um programa que:
1. Contenha uma função que receba um valor inteiro como parâmetro
2. Retorne o valor validado, ou peça um novo valor se o fornecido for inválido
"""
def validaNum():
    while True:
        num = str(input('Digite um número inteiro: '))

        if num.isnumeric():
            print(f'Validado número {num}')
            break
        else:
            print('Erro, valor inválido!')

validaNum()