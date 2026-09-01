"""
EXERCÍCIO D102 - Função para fatorial
Crie um programa que:
1. Crie uma função que receba dois parâmetros: 
    - um número, 
    - um valor booleano (opcional) indicando se o fatorial será mostrado ou não
2. Retorne o resultado fatorial desse número ou mostre o fatorial na tela, conforme o valor do segundo parâmetro
"""

def fatorial(valor, exibir=False):
    fat = valor
    escrito = f'{valor}'
    for i in range(fat-1, 0, -1):
        escrito += f' * {i}'
        fat *= i


    if not exibir:
        print(f'Valor do fatorial de {valor} = {fat}')
    else:
        print(f'{escrito} = {fat}')

n = int(input('Digite um número para calculo fatorial: '))
exibir = str(input('Deseja exibir o cálculo completo [S/N]'))

if exibir in 'Nn':
    fatorial(n)
else:
    fatorial(n, True)
