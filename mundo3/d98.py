"""
EXERCÍCIO D98 - Função de Contador
Crie um programa que:
1. Crie uma função chamada contador(), que receba três parâmetros: início, fim e passo
2. Faça a função realizar três contagens através de laços for:
    a) De 1 até 10, de 1 em 1
    b) De 10 até 0, de 2 em 2
    c) Uma contagem personalizada
"""

def contador( inicio, fim, passo):
    for i in range(inicio, fim+passo, passo):
        print(f'{i} ', end='')
    print()

contador(1, 10, 1)
contador(10, 1, -2)
