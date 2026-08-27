"""
EXERCÍCIO D51 - Progressão Aritimética (PA)
Crie um programa que:
1. Leia o Primeiro termo
2. Leia a Razão da PA
3. Ao final, demonstre os 10 primeiros dígitos dessa PA usando o "for"
"""

primTermo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
resultado = f'{primTermo}'

for  i in range(1, 10):
    primTermo += razao
    resultado += f', {primTermo}'
print(resultado)