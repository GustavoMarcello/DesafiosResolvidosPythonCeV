"""
EXERCÍCIO D101 - Função para votação
Crie um programa que:
1. Contenha uma função que recebeba como parâmetro o ano de nascimento de uma pessoa
2. Retorne um valor literal indicando se a pessoa tem:
    - voto NEGADO, (menores de 16 anos)
    - voto OPCIONAL (entre 16 e 18 anos, maiores de 65 anos)
    - voto OBRIGATÓRIO (entre 18 e 65 anos)
"""
from datetime import datetime

def validaIdadeVotacao(anoNascimento):
    anoAtual = datetime.now().year
    idade = anoAtual - anoNascimento
    if idade < 16:
        print(f'Idade {idade} anos, VOTO NEGADO')
    elif idade < 18 or idade > 65:
        print(f'Idade {idade} anos, VOTO OPICIONAL')
    else:
        print(f'Idade {idade} anos, VOTO OBRIGATÓRIO')



ano = int(input('Digite o ano de nascimento do eleitor: '))
validaIdadeVotacao(ano)