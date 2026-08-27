"""
EXERCÍCIO D57 - Validação de Inputs
Crie um programa que:
1. Leia o sexo de uma pessoa, porém apenas aceite "M" ou "F"
2. Em caso de outro valor, repita o pedido com warning de valor inválido
3. Ao final confirme o valor correto
"""

sexo = ''

while sexo == '':
    pergunta = str(input('Digite seu sexo entre [M/F]: ')).upper()
    if pergunta == 'M' or pergunta == 'F':
        sexo = pergunta
        print(f'Sexo {sexo} confirmado!')
    else:
        print('Valor inválido!')
