"""
EXERCÍCIO D97 - Função que escreve Texto em uma Caixa
Crie um programa que:
1. Crie uma função que receba um texto como parâmetro
2. Mostre o texto em uma caixa de caracteres formatados
"""
def titulo(texto):
    print('-='*20)
    print(f'{texto}'.center(40))
    print('-='*20)



titulo('Olá Mundo!')