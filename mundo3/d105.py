"""
EXERCÍCIO D105 - Gerando dicionário com funções
Crie um programa que:
1. Contenha uma função que receba várias notas de alunos,
2. Retorne um dicionário com as seguintes informações:
    - Quantidade de notas inseridas
    - Média das notas
    - Maior nota
    - Menor nota
    
obs* Adicione também docstrings
"""
def recebeNotas(*notas):
    """
    Esta função recebe diversos valores float via tupla e calcula:
    - quantidade total de valores
    - media entre os valores da tupla
    - maior valor da tupla
    - menor valor da tupla
    """
    dados = {
        'qtdNotas': len(notas),
        'media': (sum(notas) / len(notas)),
        'maiorNota': max(notas),
        'menorNota': min(notas)
    }

    return dados



print(recebeNotas(5, 4, 10, 9, 6, 7.5))
help(recebeNotas)