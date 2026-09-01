"""
EXERCÍCIO D100 - Função para sortear e somar valores
Crie um programa que:
1. Contenha uma lista e duas funções:
    a) A primeira função vai sortear 5 números e colocar dentro da lista
    b) A segunda função vai mostrar a soma entre todos os valores pares sorteados pela primeira função
"""

from random import randint

def sortear(qtdSorteios):
    sorteados = []
    for i in range(0, qtdSorteios):
        sorteados.append(randint(0, 50))
    return sorteados

def somar(valores):
    return sum(valores)



sorteados = sortear(5)

print(f'Valores sorteados: {sorteados}')
print(f'Valores somados: {somar(sorteados)}')