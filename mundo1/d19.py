"""
EXERCÍCIO D19 - Escolher um Aluno Aleatório
Crie um programa que:
1. Importe o módulo random
2. Crie uma lista com nomes de alunos
3. Use random.choice() para selecionar um aluno aleatoriamente
4. Exiba o nome do aluno escolhido
"""

import random

alunos = ['Gustavo', 'Pedro', 'Lívia', 'Ana', 'Fred']

print(f'O Aluno(a) selecionado(a) foi: {random.choice(alunos)}')