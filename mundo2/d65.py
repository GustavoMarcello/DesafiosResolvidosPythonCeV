"""
EXERCÍCIO D65 - Maior e menor
Crie um programa que:
1. Peça ao usuário para digitar vários valores inteiros
2. O programa devera continuar perguntando [S/N] se o usuáriro quer digitar outro valor
3. Ao final demonstre a média entre todos, o maior e o menor valor inserido
"""

continuar = ''
valor = 0
countValores = 0
soma = 0
listaValores = []

while continuar != 'N':
    valor = int(input('Digite um valor: '))
    listaValores.append(valor)
    countValores += 1
    soma += valor
    continuar = str(input('Deseja continuar [S/N]: ')).upper()

listaValores.sort()
print(f'Maior valor: {listaValores[-1]}')
print(f'Menor valor: {listaValores[0]}')
print(f'Média: {soma / countValores}')