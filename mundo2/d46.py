"""
EXERCÍCIO D46 - Contagem regressiva
Crie um programa que:
1. Começe uma contagem regressiva a partir de 10 até 0
2. Exiba cada número da contagem regressiva com intervalo de 1 segundo
3. Ao final, exiba "Feliz Ano Novo!"
"""

from time import sleep

for i in range(10, -1, -1):
    print(i)
    sleep(1)
print('Feliz Ano Novo!')
