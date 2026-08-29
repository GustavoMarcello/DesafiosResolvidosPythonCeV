"""
EXERCÍCIO D78 - Maior e Menor valor na Lista
Crie um programa que:
1. Leia 5 valores inteiros e guarde-os em uma lista
2. Exiba o Maior e menor valor da lista com suas respectivas posições
"""

inicio = 1
fim = 6
valores = []

for i in range(inicio, fim):
    n = int(input(f'{i}- Digite um valor: '))
    valores.append(n)

for i, v in enumerate(valores):
    if i == 0:
        maior = v
        menor = v
    else:
        if v > maior:
            maior = v
        else:
            if v < menor:
                menor = v

print(valores)
print(f'Maior valor: {maior} na posição {valores.index(maior)}')
print(f'Menor valor: {menor} na posição {valores.index(menor)}')