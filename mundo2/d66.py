"""
EXERCÍCIO D66 - Soma de inputs
Crie um programa que:
1. Peça ao usuário para digitar vários valores inteiros
2. O programa devera finalizar ao input de 999
3. Ao final demonstre o total de valores inseridos e a soma entre todos
"""
valor = 0
countValores = 0
soma = 0

while valor != 999:
    countValores += 1
    soma += valor
    valor = int(input('Digite um valor: '))

print(f'Quantidade de valores: {countValores-1}')
print(f'Soma total {soma}')