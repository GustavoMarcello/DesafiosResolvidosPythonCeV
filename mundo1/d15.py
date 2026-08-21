"""
EXERCÍCIO D15 - Cálculo de Aluguel de Carro
Crie um programa que:
1. Peça ao usuário para digitar o número de dias de aluguel
2. Peça o número de quilômetros percorridos
3. Calcule o total: (dias * 60) + (km * 0.15)
4. Exiba o valor total a pagar em reais
"""

dias = int(input('Digite o total de dias de locação do veículo: '))
kmTotal = float(input('Digite o total de Km percorridos: '))

valorTotal = (dias * 60) + (kmTotal * 0.15)

print(f'O valor total ficou R${valorTotal:.2f}')