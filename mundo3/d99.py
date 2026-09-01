"""
EXERCÍCIO D99 - Função que encontra o maior valor
Crie um programa que:
1. Crie uma função que receba vários parâmetros
2. Retorne o maior valor entre eles
"""

def maior(valores):
    valores.sort()
    return valores[-1]

numeros = []
while True:
    valor = float(input('Digite um valor: '))
    numeros.append(valor)

    continuar = str(input('Deseja continuar [S/N]: '))
    if continuar in 'Nn':
        break

print(f'O maior valor digitado foi: {maior(numeros)}')