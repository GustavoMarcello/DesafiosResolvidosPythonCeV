"""
EXERCÍCIO D44 - Gerenciador de Pagamentos
Crie um programa que:
1. Peça o preço de um produto
2. Exiba as opções de pagamento:
    - À vista em dinheiro ou cheque: 10% de desconto
    - À vista no cartão: 5% de desconto
    - Em até 2x no cartão: preço normal
    - 3x ou mais no cartão: 20% de juros
3. Calcule e exiba o valor final a ser pago de acordo com a opção escolhida
"""

preco = float(input('Digite o preço do produto: '))
pagamento = int(input('''
Opções de pagamento:
[1] À vista em dinheiro ou cheque: 10% de desconto
[2] À vista no cartão: 5% de desconto
[3] Em até 2x no cartão: preço normal
[4] 3x ou mais no cartão: 20% de juros
'''))

if pagamento == 1:
    print(f'Valor a ser pago: {preco*0.9} reais')
elif pagamento == 2:
    print(f'Valor a ser pago: {preco*0.95} reais')
elif pagamento == 3:
    print(f'Valor a ser pago: {preco} reais')
else:
    print(f'Valor a ser pago: {preco*1.2} reais')
