"""
EXERCÍCIO D72 - Analisando dados em uma Tupla
Crie um programa que:
1. leia 4 valores inteiros pelo teclado e guarde-os em uma tupla
2. no final, mostre:
    a) quantas vezes apareceu o valor 9
    b) em que posição foi digitado o primeiro valor 3
    c) quais foram os números pares
"""

numeros = (
    int(input('Digite o primeiro valor: ')),
    int(input('Digite o segundo valor: ')),
    int(input('Digite o terceiro valor: ')),
    int(input('Digite o quarto valor: '))
)

print(f'O número 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O número 3 está na posição {numeros.index(3)+1}')
else:
    print('Não foi digitado o número 3')

pares = ''
for n in numeros:
    if n % 2 == 0:
        pares += f'{n}  '
print(f'Números pares: {pares}')

