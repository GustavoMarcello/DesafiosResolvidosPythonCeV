"""
EXERCÍCIO D62 - Progressão Aritimética (PA)
Crie um programa que:
1. Leia o Primeiro termo
2. Leia a Razão da PA
3. Demonstre os 10 primeiros dígitos dessa PA usando o "for"
4. Ao final pergunte quantos mais dígitos o usuário quer visualizar
5. Encerre o programa ao usuário digitar 0
"""

primTermo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
resultado = f'{primTermo}'

for  i in range(1, 10):
    primTermo += razao
    resultado += f', {primTermo}'
print(resultado)

maisDigitos = 1
while maisDigitos != 0:
    maisDigitos = int(input('Digite quantos digitos a mais da PA você deseja visualizar: '))
    for i in range(0, maisDigitos):
        primTermo += razao
        resultado += f', {primTermo}'
    print(resultado)