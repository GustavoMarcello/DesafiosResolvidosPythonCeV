"""
EXERCÍCIO D20 - Embaralhar Ordem de Alunos
Crie um programa que:
1. Importe o módulo random
2. Crie uma lista com nomes de alunos
3. Use random.shuffle() para embaralhar a ordem da lista
4. Exiba a ordem aleatória dos alunos
"""

import random

alunos = ['Gustavo', 'Pedro', 'Lívia', 'Ana', 'Fred']
random.shuffle(alunos)

print(f'Lista de alunos embaralhados: {alunos}')