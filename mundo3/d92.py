"""
EXERCÍCIO D92 - Cadastro de Trabalhador em Python
Crie um programa que:
1. Leia o nome, ano de nascimento e carteira de trabalho de um trabalhador
2. Se a carteira de trabalho for diferente de 0:
    - Leia o ano de contratação e o salário
3. Calcule e acrescente, além da idade, o ano de aposentadoria
"""

from datetime import datetime

dados = {}
anoAtual = datetime.now().year

dados['nome'] = str(input('Digite o nome do trabalhador: '))
ano = int(input('Digite o ano de nascimento do trabalhador: '))
dados['idade'] = anoAtual - ano
dados['ctps'] = int(input('Digite o número da carteira de trabalho CTPS: '))

if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Digite o ano de contratação (0 não tem): '))
    dados['salario'] = float(input('Digite o salário: '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratacao'] + 35) - anoAtual)

print(dados)